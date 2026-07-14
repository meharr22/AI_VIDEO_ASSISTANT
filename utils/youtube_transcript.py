from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url: str) -> str:
    parsed_url = urlparse(url)

    if parsed_url.hostname in ["youtu.be", "www.youtu.be"]:
        return parsed_url.path.lstrip("/")

    if parsed_url.hostname in [
        "youtube.com",
        "www.youtube.com",
        "m.youtube.com"
    ]:
        if parsed_url.path == "/watch":
            return parse_qs(parsed_url.query)["v"][0]

        if parsed_url.path.startswith("/shorts/"):
            return parsed_url.path.split("/")[2]

        if parsed_url.path.startswith("/embed/"):
            return parsed_url.path.split("/")[2]

    raise ValueError("Invalid YouTube URL")


def get_youtube_transcript(url: str) -> str:
    video_id = extract_video_id(url)

    api = YouTubeTranscriptApi()

    transcript = api.fetch(video_id)

    text = " ".join(
        snippet.text
        for snippet in transcript
    )

    return text