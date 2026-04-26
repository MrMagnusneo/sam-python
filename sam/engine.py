from typing import Optional

from .samtts_native import SamTTS


def _pcm_u8_to_wav(audio_u8: bytes, sample_rate: int = 22050) -> bytes:
    data_size = len(audio_u8)
    riff_size = 36 + data_size
    header = bytearray()
    header.extend(b"RIFF")
    header.extend((riff_size & 0xFFFFFFFF).to_bytes(4, "little"))
    header.extend(b"WAVE")
    header.extend(b"fmt ")
    header.extend((16).to_bytes(4, "little"))  # PCM header size
    header.extend((1).to_bytes(2, "little"))   # PCM format
    header.extend((1).to_bytes(2, "little"))   # mono
    header.extend((sample_rate).to_bytes(4, "little"))
    header.extend((sample_rate).to_bytes(4, "little"))  # byte rate (8-bit mono)
    header.extend((1).to_bytes(2, "little"))   # block align
    header.extend((8).to_bytes(2, "little"))   # bits per sample
    header.extend(b"data")
    header.extend((data_size & 0xFFFFFFFF).to_bytes(4, "little"))
    return bytes(header) + audio_u8


class SamPythonEngine:
    def __init__(self, speed=72, pitch=64, mouth=128, throat=128, singmode=False, phonetic=False):
        self.speed = int(speed)
        self.pitch = int(pitch)
        self.mouth = int(mouth)
        self.throat = int(throat)
        self.singmode = bool(singmode)
        self.phonetic = bool(phonetic)

    def synthesize_raw(self, text: str, phonetic: Optional[bool] = None, sample_rate: int = 22050) -> bytes:
        sam = SamTTS(
            speed=self.speed,
            pitch=self.pitch,
            mouth=self.mouth,
            throat=self.throat,
            sing_mode=self.singmode,
        )
        return bytes(
            sam.get_audio_data(
                input_data=text,
                phonetic=self.phonetic if phonetic is None else bool(phonetic),
                sample_rate=sample_rate,
            )
        )

    def synthesize_wav(self, text: str, phonetic: Optional[bool] = None) -> bytes:
        raw = self.synthesize_raw(text=text, phonetic=phonetic, sample_rate=22050)
        return _pcm_u8_to_wav(raw, sample_rate=22050)
