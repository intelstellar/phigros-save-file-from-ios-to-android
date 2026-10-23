# phigros-save-file-from-ios-to-android
i just figured out there is https://phibot.dev that can be used to transfer data from unverified taptap cn account (from ios) to taptap global account (to android), but since the cloud save feature in phigros global is going to be discontinued soon, i'll write a tutorial about how to do it manually (if u cant create an taptap cn account or u cannot login into your taptap cn account due to chinese citizen id verification)

Preparation
- your iphone (must be jailbroken & with filza file explorer installed)
- your android phone (also must be rooted)
- a functionable computer (with latest python installed on your computer)
- https://plist-viewer.com/ (to convert the save file into readable version)
- converter.py from this repo (to make the savefile compatible with phigros in android)

step 1: download the converter
step 2: open iphone -> open filza file manager -> follow this directory path `/var/mobile/Containers/Data/Application/Phigros/Library/Preferences/` -> find a file named `games.Pigeon.Phigros.plist` (this is the savefile), then u will have to transfer this file to your computer (upload it to your google drive is the easiest way)
step 3: after successfully transfer the savefile to your computer, open https://plist-viewer.com/ and drag your savefile into this website, then click on save file to xml button (the third button on the top left) to save it, then change your file name to `ios_save.plist` (very necessary)
step 4: now u have to make sure that the ios_save.plist and the converter.py is in the same folder, then open a command prompt, type "py converter.py" then press enter and boom, now you have your savefile that is completely compatible with phigros android
step 5: now with your savefile, u have to put it into your phigros game folder on android, for more detail u can read [this](https://docs.google.com/document/d/146J1Y0lNBkfpGsPZXp1gghk7dDFI3nK5_CWPtTTpHHo/edit?tab=t.7wadztfqe0tr) (basically copy your savefile into `/data/data/com.PigeonGames.Phigros/shared_prefs` and it's based on the phigros you have on your phone is global version or chinese version)
step 6: launch game and enjoy!

p/s: https://www.reddit.com/r/jailbreak/comments/tc68ky/discussion_i_found_an_app_that_can_explore_ios/#lightbox found this on reddit, so basically there is a way to get your savefile from your iphone without jailbreaking it, but i haven't tried yet so i'm not really sure if it's gonna work)
if you have any question, feel free to send me a msg to my discord lol (check my github readme)

<img width="1536" height="1920" alt="image" src="https://github.com/user-attachments/assets/8555b091-f0b0-4874-86bf-d8a5deaf8274" />
(found this randomly on pigeon discord so idk where the source is)
