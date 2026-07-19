from pathlib import Path


START_TOKEN = "<START>"
END_TOKEN = "<EOS>"


def load_image_list(path: str) -> list[str]:
    path = Path(path)

    with path.open("r", encoding="utf-8") as file:
        return [
            line.strip()
            for line in file
            if line.strip()
        ]


def read_image_descriptions(path: str ) -> dict[str, list[list[str]]]:

    path = Path(path)
    descriptions: dict[str, list[list[str]]] = {}

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            fields = line.strip().split()

            if not fields:
                continue

            caption_id = fields[0]
            image_name = caption_id.split("#", maxsplit=1)[0]

            caption_tokens = [
                START_TOKEN,
                *(token.lower() for token in fields[1:]),
                END_TOKEN,
            ]

            descriptions.setdefault(image_name, []).append(
                caption_tokens
            )

    return descriptions


def get_max_caption_length(image_names: list[str],descriptions: dict[str, list[list[str]]],) -> int:
    return max(
        len(caption)
        for image_name in image_names
        for caption in descriptions[image_name]
    )