from collections.abc import Iterable, Sequence


PAD_TOKEN = "<PAD>"
START_TOKEN = "<START>"
END_TOKEN = "<EOS>"

PAD_ID = 0
START_ID = 1
END_ID = 2


class Vocabulary:
    def __init__(self, word_to_id: dict[str, int], id_to_word: dict[int, str],) -> None:
        self.word_to_id = word_to_id
        self.id_to_word = id_to_word

    @classmethod
    def build(
        cls,
        captions: Iterable[Sequence[str]],) -> "Vocabulary":
        
        
        special_tokens = {PAD_TOKEN,START_TOKEN,END_TOKEN,}

        words = {
            token
            for caption in captions
            for token in caption
            if token not in special_tokens}

        sorted_words = sorted(words)

        word_to_id = {
            PAD_TOKEN: PAD_ID,
            START_TOKEN: START_ID,
            END_TOKEN: END_ID,
        }

        for word in sorted_words:
            word_to_id[word] = len(word_to_id)

        id_to_word = {
            token_id: token
            for token, token_id in word_to_id.items()
        }

        return cls(
            word_to_id=word_to_id,
            id_to_word=id_to_word,
        )

    def __len__(self) -> int:
        return len(self.word_to_id)

    def encode(self, tokens: Sequence[str]) -> list[int]:
        return [
            self.word_to_id[token]
            for token in tokens
        ]

    def decode(self, token_ids: Sequence[int]) -> list[str]:
        return [
            self.id_to_word[token_id]
            for token_id in token_ids
        ]