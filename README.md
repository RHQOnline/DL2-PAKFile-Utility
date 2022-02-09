# Dying Light 2 PAKFile Utility
A **Dying Light 2 (DL2) PAKFile Utility** for **Modders** and **Mod Makers**.<br>
This tool aims to make PAKFile modding a breeze for both Dying Light 2 modders and mod makers.<br>
See the [Roadmap](https://github.com/RHQOnline/DL2-PAKFile-Utility#roadmap) for a better idea of what's to come!<br>
_More TBA Soon_.

# Features
- [x] Ability to Examine PAKFiles (see size, validity, and any CRC / Header mismatch errors)
- [x] Ability to Extract PAKFiles into a Folder to Edit
- [x] Ability to Build a PAKFile from a Folder
- [x] Incredibly Efficient Mod Builder with 79% (21% of Original Size) [LZMA Compression](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm) on the size of the mods!

# Known Bugs / Issues
This is a collective list of known bugs / glitches / issues.
 * None / TBA

# Running the Utility
## As an Executable / Binary
Step-by-step instructions to running the utility as a standalone executable.
1. Download the [Latest Release](https://github.com/RHQOnline/DL2-PAKFile-Utility/releases/latest) from GitHub.
2. Save it somewhere easy to remember. A mod management folder is recommended.
3. Right-Click the `DL2-PAKFile-Utility.exe` File and Select `Run as Administrator`
4. Follow the On-Screen Prompts
## From Source
Step-by-step instructions to running the utility from source.
1. Open an Elevated Command Prompt
2. Make a Virtual Environment and Activate it
3. `pip install -r requirements.txt`
4. `python main.py`
5. ???
6. $$ PROFIT $$

# Making Mods
The location of the two default PAKFiles (`data0.pak` and `data1.pak`) is `<Steam Install>\steamapps\common\Dying Light 2\ph\source`. Opening these PAKFiles and extracting them allows you to see all of the scripts that run in the game's engine, the [C-Engine](https://en.wikipedia.org/wiki/Dying_Light_2_Stay_Human#Development). To make a mod, extract one of these PAKFiles and then simply find the files inside of the extracted contents that include what you wish to change, modify them how you'd like, delete everything else that *wasn't* changed, and then build a PAKFile from that folder! To use the mod you've made, build it as `dataN.pak` where `N` is the next highest available number in your default PAKFile location (for example, if you only have `data0.pak` and `data1.pak`, you'd build a `data3.pak`). If other users wish to use it and they have a different number of PAKFiles than you, they may simply rename it to be a higher number in the filename.
## Theory on Mod Loading Order
As writing a new mod makes use of upping the integer in the `dataN.pak` filenames, I'm assuming the higher the integer, the higher the order of precedence is. This is perhaps to say, for example, if one mod (`data3.pak`) gives unlimited stamina and another (`data4.pak`) removes unlimited stamina, I believe `data4.pak`'s effects would take priority over `data3.pak`'s and would render stamina untouched / not unlimited.

# FAQ
**Q1: Why does this need to be ran as an administrator?**<br>
**A1: Some people store their games / mod management folders in weird places that non-elevated applications typically can't access. This is simply insurance on that possibility, making sure _any user_ who stores their files _anywhere_ can use this tool!**

# Roadmap
This is a loose outline of what is in the future for the DL2 PAKFile Utility!
- [x] Ability to Examine PAKFiles (see size, validity, and any CRC / Header mismatch errors)
- [x] Ability to Extract PAKFiles into a Folder to Edit
- [x] Ability to Build a PAKFile from a Folder
- [x] Incredibly Efficient Mod Builder with 79% (21% of Original Size) [LZMA Compression](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm) on the size of the mods!
- [ ]  GUI Integration
- [ ]  Intelligently Browse DL2 PAKFile Folder Contents
- [ ]  Detailed Documentation for both the Application and for Modding DL2
- [ ]  Auto-Updating Feature for the Utility that Pulls from GitHub
- [ ]  More Modding Tools Built-In

More to be Announced Soon!
