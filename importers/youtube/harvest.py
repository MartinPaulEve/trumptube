from googleapiclient.discovery import build
import json
import os.path
from YTparser import YouTubeParser

class Harvester():
    def __init__(self):
        """
        Setup and build a Youtube query object.
        Your youtube API token should go in credentials.txt in the importers/youtube directory
        """
        with open("credentials.txt", "r") as creds:
            self.api_key = creds.read()

        self.service = build('youtube', 'v3', developerKey=self.api_key)

    def get_comment_threads(self, video_id):
        """
        Fetches top-level comments for a video ID
        :param video_id: The ID of the video
        :return: The dictionary of comments
        """

        results = self.service.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText"
        ).execute()

        return results["items"]

    def get_comments(self, parent_id):
        """
        Fetches a thread of comment replies
        :param parent_id: The parent comment ID
        :return: The dictionary of reply comments
        """
        results = self.service.comments().list(
            part="snippet",
            parentId=parent_id,
            textFormat="plainText"
        ).execute()

        return results["items"]


if __name__ == "__main__":
    harvester = Harvester()

    with open("sources.txt", "r") as videos:

        sources = videos.readlines()

        for source in sources:
            video_id = source

            fname = "output/{0}.json".format(video_id)

            str_out = ""

            if os.path.isfile(fname):
                json = json.load(open(fname, "r"))
                print("Skipping {0} as it already exists.".format(fname))
            else:
                print("Harvesting into {0}.".format(fname))
                results = harvester.get_comment_threads(video_id)

                json_out = {}
                json_out['thread'] = results

                for res in results:
                    str_out = str_out + " " + res["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                    json_out[res['id']] = harvester.get_comments(res['id'])

                    for sub_res in json_out[res['id']]:
                        str_out = str_out + " " + sub_res["snippet"]["textDisplay"]

                with open(fname, "w") as json_writer:
                    json_writer.write(json.dumps(json_out, ensure_ascii=False))

            # now pass this to the parser
            yt = YouTubeParser()

            yt.parse(str_out, "output/{0}.csv".format(video_id))
