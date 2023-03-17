# OpenLP to ProPresenter Converter

This repository contains a script that converts OpenLP XML song exports into a format recognized by ProPresenter.

## Prerequisites

- Python 3.x

## Usage

1. Export your songs from OpenLP as XML files (see instructions below).
2. Place the exported XML files in the `input` folder.
3. Run the script: `python converter.py`
4. The converted song files will be available in the `output` folder as plain text files.

## Export Songs from OpenLP

OpenLP has the ability to export your songs in the OpenLyrics worship song format. This is convenient for transferring your songs to another computer or for backup purposes.

To export songs from OpenLP, follow these steps:

1. Open OpenLP.
2. Click "File" > "Export" > "Song" in the top menu.
3. Click "Next" in the dialog box that appears.
4. Select the songs you want to export by clicking on each song.
5. Use the "Search" field to search for a song title or keyword in a title.
6. Click "Uncheck All" to unselect all songs, or "Check All" to select all songs.
7. Click "Next" when you have finished selecting songs.
8. Select the directory where you want the songs to be saved (e.g., the `input` folder in this repository).
9. Click "Finish" to complete the export process.

## Import Songs into ProPresenter

1. Open ProPresenter.
2. Click on "File" > "Import" > "Text File" in the top menu.
3. Navigate to the `output` folder in this repository.
4. Select the converted text files and click "Open."
5. ProPresenter will import the songs and make them available in your library.

## Sample Folders

- `input_sample`: Contains sample OpenLP XML song exports.
- `output_sample`: Contains sample converted song files compatible with ProPresenter.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
