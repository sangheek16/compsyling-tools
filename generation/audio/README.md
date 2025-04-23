# 🎧 Auditory Stimulus Generation

This folder contains scripts for generating and processing audio stimuli—from text-to-speech synthesis to forced alignment and region-based chunking for experimental use.

---

## 📋 Workflow

0. **Try it out quickly**  
   `tts-gtts.py` – A minimal example for generating audio from text input using gTTS.  
   _(Functionally equivalent to `audio-stimuli.py`.)_

1. **Create audio file**  
   `audio-stimuli.py` – Generates `.mp3` files from input text using TTS (e.g., gTTS)

2. **Make TextGrid manually**  
   `combined.praat` – Open in Praat to align full sentences  
   - If your audio directory is `/input`, use `.mp3` files (this is the default)  
   - If it's `/output`, use `.wav` files instead

3. **Chunk audio file by sentence**  
   `csv-to-textgrid.py` – Uses the TextGrid and input `.csv` to create region-level segmentations

4. **Change audio file extension**  
   `mp3-to-wav.py` – Converts `.mp3` to `.wav`, required for MFA

5. **Run MFA (Montreal Forced Aligner)**  
   - [MFA tutorial](https://lingmethodshub.github.io/content/tools/mfa/mfa-tutorial/#running-the-aligner)  
   - `.wav` format is required to run the aligner

6. **Convert chunked TextGrid to a `.csv`**  
   `get-intervals.py` – Extracts interval timing from the `.TextGrid` (use the one from `/output`)

7. **Clean & annotate regions**  
   `combine-audioLen.py` – Removes misassigned 'pause' rows and assigns region numbers

---

Each script is modular and can be adjusted depending on your experiment’s audio setup or input format.