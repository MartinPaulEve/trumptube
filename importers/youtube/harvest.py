from googleapiclient.discovery import build
from googleapiclient.discovery import build_from_document


class Harvester():
    def __init__(self):
        with open("credentials.txt", "r") as creds:
            self.api_key = creds.read()

        self.service = build('youtube', 'v3', developerKey=self.api_key)

    def get_comment_threads(self):
        with open("sources.txt", "r") as videos:
            sources = videos.readlines()

            for source in sources:
                video_id = source

                results = self.service.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    textFormat="plainText"
                ).execute()

                for item in results["items"]:
                    comment = item["snippet"]["topLevelComment"]
                    author = comment["snippet"]["authorDisplayName"]
                    text = comment["snippet"]["textDisplay"]
                    print("Comment by %s: %s" % (author, text))

                return results["items"]

    # Call the API's comments.list method to list the existing comment replies.
    def get_comments(self, parent_id):
        results = self.service.comments().list(
            part="snippet",
            parentId=parent_id,
            textFormat="plainText"
        ).execute()

        for item in results["items"]:
            author = item["snippet"]["authorDisplayName"]
            text = item["snippet"]["textDisplay"]
            print("Comment by %s: %s" % (author, text))

        return results["items"]


if __name__ == "__main__":
    harvester = Harvester()
    results = harvester.get_comment_threads()
    for res in results:
        harvester.get_comments(res['id'])