<!-- omit in toc -->
# DiscoDOS Installation

- [Install released version](#install-released-version)
  - [Windows](#windows)
  - [macOS/Linux](#macoslinux)
- [Configure Discogs collection access](#configure-discogs-collection-access)
- [DiscoDOS Setup - Troubleshooting](#discodos-setup---troubleshooting)
- [Configure _discosync_ - The DiscoDOS backup & sync tool](#configure-discosync---the-discodos-backup--sync-tool)
  - [Configure Dropbox Access for _discosync_](#configure-dropbox-access-for-discosync)
  - [Configure a webserver folder for _discosync_](#configure-a-webserver-folder-for-discosync)


There are two ways of installing DiscoDOS:

- Released version (get a program that just works, is easy to install and well tested)
- Development version (get the latest features, contribute to DiscoDOS by trying out new things and reporting back what you think. I usually try to keep things stable in the master branch. I use it myself on my production database, so it just has to work. Seldomely there will be major bugs that really could corrupt your data. In any case make sure you use DiscoDOS' neet built-in backup/sync feature!). There is a separate document about [installing the development version](https://github.com/JOJ0/discodos/blob/master/CONTRIBUTION.md).


## Install released version

basically the steps on every OS are similar:

* download package
* unpack
* launch DiscoDOS setup
  * a local database will be initialized (the DiscoBASE)
  * the DiscoDOS CLI tools will be set up for your user environment
* configure Discogs collection access


### Windows

download the latest Windows package from the [release page](https://github.com/JOJ0/discodos/releases)

unpack - it contains a folder named `discodos`.

You can move the `discodos` folder whereever you like on your sytem. If unsure or not too familiar with command line tools I suggest you just put it directly into your users "home folder" (`c:\Users\your_name\discodos`).

Start a command prompt window (start button - cmd.exe - enter). Change into the discodos folder and see what's in there:

```
cd discodos
dir
```

You should see 4 files: `cli.exe`, `winconfig.exe`, `sync.exe` and `config.yaml`

Launch DiscoDOS setup - a local **database** (the so-called DiscoBASE) and **some additional files** (the so-called DiscoDOS command line tools) will be created. Type the following into your command prompt window:

`winconfig`

Configure access to your Discogs collection as described in chapter [Configure Discogs collection Access](#configure-discogs-collection-access), then come back here!

Start using DiscoDOS by double clicking the newly created batch file `discoshell.bat` - make a shortcut to it on your Desktop.

Launch the `disco` command - if the connection to your Discogs collection is working it will ask you to view a little tutorial teaching you how it works - answer the question with "y" and follow the steps.

If you have any troubles or questions arise, please read chapter [DiscoDOS Setup - Troubleshooting](#discodos-setup---troubleshooting), it is an in-detail explanation of what the DiscoDOS setup script (winconfig.exe) does and what differences there are between operating systems.

Your starting point for further documentation is the [Readme and User's manual page](https://github.com/JOJ0/discodos/blob/master/README.md#importing-your-discogs-collection). Your next step will be to import your Discogs collection.


### macOS/Linux

download the latest macOS or Linux package from the
[release page](https://github.com/JOJ0/discodos/releases)

unpack - on a Mac just double click the tar.gz file, it will extract a folder named `discodos`. On Linux do something like this:

```
tar xvzf discodos-1.0-rc1-macOS.tar.gz
ls -l discodos
```

You can move the `discodos` folder whereever you like on your sytem. If unsure or not too familiar with command line tools I suggest you just put it directly into your users "home folder" (on a Mac: `/Users/your_name/discodos`).

Assuming your discodos folder resides directly in your home folder, start a terminal, if you haven't already (on Mac: Applications - Utilities - Terminal.app). Jump right into the discodos folder and see what's in there:

```
cd discodos
ls -l
```

You should see 3 files: `cli`, `setup`, `sync` and `config.yaml`

Launch DiscoDOS setup - a local **database** (the so-called DiscoBASE) and **some additional files** (the so-called DiscoDOS command line tools) will be created. Type the following into your terminal window:

`./setup`

Execute the following provided script to customize the CLI tools for your user environment:

`./install_wrappers_to_path.sh`

Configure access to your Discogs collection as described in chapter [Configure Discogs collection access](#configure-discogs-collection-access), then come back here!

If everything seems fine, launch the `disco` command - if the connection to your Discogs collection is working it will ask you to launch a little tutorial teaching you how it works - answer the question with "y" and follow the steps.

If you have any troubles or questions arise, please read chapter [DiscoDOS Setup - Troubleshooting](#discodos-setup---troubleshooting), it is an in-detail explanation of what the DiscoDOS setup script does and what differences there are between operating systems.

Your starting point for further documentation is the [Readme and User's manual page](https://github.com/JOJ0/discodos/blob/master/README.md#importing-your-discogs-collection). Your next step will be to import your Discogs collection.


## Configure Discogs collection access

To access your Discogs collection you need to generate an API login token and put it into the configuration file.

- Login to discogs.com
- Click your avatar (top right)
- Select _Settings_
- Switch to section _Developers_
- Click _Generate new token_
- Open the file `config.yaml` (inside the discodos root folder, next to the files `setup.py` and `cli.py`) and copy/paste the generated Discogs token into it:
  - on Windows right click the file - select "Open With" - choose "Notepad" - paste token to the right place (as shown below).
  - on Mac secondary click/tab (two fingers) - select "Open With" - chooose "TextEdit.app" - paste token to the right place (as shown below).

The line in config.yaml should look something like this then (watch out for the surrounding quotes):

 ```
 discogs_token: 'XDsktuOMNkOPxvNjerzCbvJIFhaWYwmdGPwnaySH'
 ```

- Save and close the file
- Jump back to [Windows installation chapter](#windows)
- Jump back to [macOS/Linux installation chapter](#macoslinux)


## DiscoDOS Setup - Troubleshooting

If you have followed the installation steps in above chapters already, you don't have to read through this chapter. It points out what exactly the DiscoDOS setup script does and explains operating system differences. If you had any troubles with above installation steps, it makes sense your read through here though.

_**Make sure you are in DiscoDOS' root folder (usually: `your_homefolder/discodos`)**_

Launch DiscoDOS setup and carefully read the output (add .py if installing development version)

`./setup`

On Windows, DiscoDOS setup is launched like this:

`winconfig.exe`

Hints if you are about to set up the development version:

* double check the setup command - it's slightly different: `./setup.py`
* Make sure the Python environment you created in the [Development version installation instructions](#development-version) is activated.
* On Windows make sure you have the "py launcher" installed and .py files associated (see setup notes above).
* Also on Windows it could happen that *py launcher* is not properly installed - Work around this issue by launching setup.py with python.exe:
  `python setup.py`

On **first launch**, setup just creates a config file for you named `config.yaml` (release versions have this file included already in the package, so this step doesn't apply and step two below immediately happens!`)

On **second launch**, it does several things:

- it creates an empty database -> you should find a file named `discobase.db` in your discodos folder.
- it sets up the DiscoDOS CLI commands
  - Linux/MacOS -> files `disco` `discosetup`, `discosync` and `install_wrappers_to_path.sh` in your discodos folder.
  - Windows -> files `disco.bat`, `discosetup.bat`, `discosync.bat` and `discoshell.bat`

_**If setup ran through you can try launching `disco` for the first time :-)**_

On **Windows** your starting point always is double-clicking `discoshell.bat` first. A new command prompt window named "DiscoDOS shell" is opened and the "Virtual Python Environment", DiscoDOS needs to function, is activated. Once inside the shell, execute CLI commands via the `disco.bat` wrapper. As usual on Windows systems you can leave out the `.bat` ending and just type `disco`.

On **Linux and macOS** the workflow is slightly different: To execute DiscoDOS commands, fire up your favorite terminal application and just type `./disco`. (Note if using the development version: This wrapper script also takes care of activating the "Virtual Python Environment"). To conveniently use the `disco` command from everywhere on your system, execute the provided script `./install_wrappers_to_path.sh`

_The following commands assume that, depending on your OS, you are either inside the DiscoDOS shell window or `disco` is being found via the PATH variable (because you've launched `installed_wrappers_to_path.sh` already)._

 Check if the database is working by creating a new mix:

`disco mix my_mix -c`

View your (empty) mix.

`disco mix my_mix`

There is two more commands you should be able to run by now:

* `discosetup` - this is just a wrapper to the setup script you just executed above, you will use it seldomly, it's used for future DiscoDOS updates and fixing things.
* `discosync` - this is the DiscoDOS backup & sync tool - you can also use it to sync the database file between different computers (either via dropbox or a webdav enabled folder on a webserver)





## Configure _discosync_ - The DiscoDOS backup & sync tool

`discosync` works with timestamps (local modification time) of the database file. It will never backup a file that has been already backuped up. Even if the file has been shared to another computer, it will only be overwritten if its contents was changed. This is to reduce the amount of (useless) backup files in your dropbox account or on your webserver.

The format of files always is "database_name_YYYY-MM-DD_HHMMSS.db"


### Configure Dropbox Access for _discosync_

To prepare your Dropbox account and DiscoDOS configuration, do the following:

- We need to create a new "Dropbbox App" in your account: https://www.dropbox.com/developers/apps/create
- Step 1: "Choose an API" - select "Dropbox API"
- Step 2: "Choose the type of access you need" - select "App folder"
- Step 3: "Name your app" - enter "discodos"
- Click "Create app"
- Scroll down to section "OAuth 2" - Click the "Generate" button right below "Generated access token"
- Double click and copy the token to the clipboard
- Put the token into the config.yaml file on all the computers you would like to use this DiscoBASE.
  - open with TextEdit.app on Mac
  - open with Notepad on Windows.

The line in config.yaml should then look something like this (watch out for the surrounding quotes):

```
dropbox_token: 'abcxyzabcxyzabcxyzabcxyzabcxyzabcxyzabcxyz'
```

- Jump back to [I'd like to use my DiscoBASE on multiple computers](README.md#id-like-to-use-my-discobase-on-multiple-computers)

If you want to delete your Dropbox app again or generate a new token because you lost it, go to the [Dropbox app console](https://www.dropbox.com/developers/apps?_tk=pilot_lp&_ad=topbar4&_camp=myapps).

Certainly you can also access the backup files via the Dropbox webinterface - Click the "discodos" app on the home screen - you will find a subfolder "discodos" containing all your backed up DiscoBASE files.


### Configure a webserver folder for _discosync_

If you don't like saving your stuff to Dropbox and happen to have your own personal webspace somewhere, `discosync` can use it to save backups. The folder needs to have these features enabled:

- [WebDAV](#https://en.wikipedia.org/wiki/WebDAV)
- Password restriction ([HTTP Basic Access Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication))

Even though it is not mandatory, the following is highly recommended to securly transport your password over the wire:

- Webserver running SSL (https://...)

Configuration steps may vary, if you can't do above configurations in your webhosters "configuration console" try contacting their support.

If you have (root) access to your server and it's an Apache webserver, configuration of a suitable folder looks like this:

```
   <Directory /var/www/discodos/>
      AllowOverride None
      DAV On
      AuthType "Basic"
      AuthName "Restricted Area"
      AuthBasicProvider file
      AuthUserFile "/etc/apache2/.htaccess_discodos"
      Require user my_discosync_user
   </Directory>
```

To create the password file:

```
htpasswd -c /etc/apache2/.htaccess_discodos my_discosync_user
```

Test if accessing your backup space is working with your webbrowser: https://www.yourdomain.com/discodos/. Usually a popup asks you for your credentials.

If everything's fine adjust your DiscoDOS configuration file (`config.yaml`)

```
webdav_user: 'my_discosync_user'
webdav_password: 'secret123'
webdav_url: 'https://www.yourdomain.com/discodos/'
```
