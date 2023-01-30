Cheat Sheet
===========

This page will serve as an area to easily access commands, snippets of codes for Git, ROS2 and Bash command line. These will be commands that we find useful or use often. If there is something
that you think will be useful to you or your classmates, let us know and we will add it in.

Command Line
-------------

There is a lot you can do with the terminal in linux, we will just cover the basics to keep it brief.

Listing and Changing Directories 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To find which directory you are in you can run the command

.. code-block:: bash

    pwd


You can do is list all files and directories in your current directory.

.. code-block:: bash

    ls

If you want to look for hidden files, you can add the option as follows:

.. code-block:: bash

    ls -a

To change into a different directory, run the following.

.. code-block:: bash

    cd <dir-name>

To change to the home directory you can simply do:

.. code-block:: bash

    cd

To change to a directory in the home directory:

.. code-block:: bash

    cd ~/<dir-name>

To change to a directory in another directory, you can write the following:

.. code-block:: bash

    cd <upper-dir>/<lower-dir>

Creating and Removing Directories and Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To make a directory, command the following:

.. code-block:: bash

    mkdir <dir-name>

You can also make multiple directories using the following.

.. code-block:: bash

    mkdir <dir1> <dir2> <dir3>

You can remove files by executing the following command

.. code:: bash

    rm <filename>

Removing a directory is as simple, run the following:

.. code-block:: bash

    rm -r <dir-name>

You can remove multiple directories the same way as making them.

.. code-block:: bash

    rm -r <dir1> <dir2> <dir3>

To create a file you can command as such:

.. code-block:: bash

    touch <filename>.<extension>

An example of this would be:

.. code-block:: bash

    touch test.py

Bash has a couple of inbuilt editors, one of them is ``nano``. To use this editor on a file command the following:

.. code-block:: bash

    nano <file-name>

To exit out of this file, command ``Ctrl+X``.

SSH Into Another Computer
^^^^^^^^^^^^^^^^^^^^^^^^^

You can ``ssh`` into computer, which is basically connecting to them remotely over a local network (Remote networks can be achieved as well through a VPN). You will need to enable ssh on the computer being connected to before you can do this.
To ssh into a computer you will need to run the following command.

.. code-block:: bash

    ssh <user>@<address>

An example of this would be

.. code-block:: bash

    ssh admin@192.168.0.1

It will then prompt you to enter a password, which will be the same as your login password onto the computer. In the case of AV1tenth cars, they will be set for you.

.. warning:: Do not do this over a publc network, it is generally unsafe.

Installing Packages
^^^^^^^^^^^^^^^^^^^

There are two package managers in bash that are installed by default, they are ``apt`` and ``snap``.

To install a package with ``apt``, run the following:

.. code-block:: bash

    sudo apt install <package-name>

To install packages with ``snap``:

.. code-block:: bash

    sudo snap install <package-name>

We will be using mainly apt package manager.

To update the package lists, command the following:

.. code-block:: bash

    sudo apt update

To upgrade packages that were updated, run the following:

.. code-block:: bash

    sudo apt upgrade

Sometimes you will need to add ``GPG`` keys to your apt sources to install certain packages, usually whatever package you are trying to install will tell you how to do it.
    
ROS2
----

ROS2 has a couple of bash commands that are required to make it run. If you haven't added a source script to the ``.bashrc`` file yet you will need to run the following command.

.. code-block:: bash

    source /opt/ros/foxy/setup.bash

To add this to your ``.bashrc`` run the following:

.. code-block:: bash

    echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc

This will source ROS2 everytime you open a terminal.

To run a package and executable in ROS, run the following.

.. code-block:: bash

    ros2 run <package-name> <executable-name>

ROS2 Packages
^^^^^^^^^^^^^

.. note:: Whenever something like ``<package-name>`` or ``<node-name>`` is written, you will replace this with the specific node or package name that you are 
    interested in.

ROS2 places its programs in directories called packages. Packages can be created using the following command.

.. code-block:: bash

    ros2 pkg create --build-type ament_python <package-name>

This is specifically for creating python packages. This creates all the necessary files and connections. You will still have to put in your program and add the correct information
to the ``setup.py``. You can list all the executables inside a package using the following command,

.. code-block:: bash

    ros2 pkg executables <package-name>

ROS2 Nodes
^^^^^^^^^^

ROS2 runs its programs as something called nodes. To see a full list of nodes, the following command can be run.

.. code-block:: bash

    ros2 node list

To find out more info about a particular node you can run,

.. code-block:: bash

    ros2 node info <node-name>

ROS2 Topics
^^^^^^^^^^^

A useful debugging tool in ros is ``topic list`` and ``topic echo``. They can be run with the following commands.

.. code-block:: bash

    ros2 topic list
    ros2 topic echo <topic-name>

``topic list`` provides a list of running topics. ``topic echo`` echoes the topic that you select.

.. code-block:: bash

    ros2 topic hz

``topic hz`` will give you the publish speed of the topic.

ROS2 Launch
^^^^^^^^^^^

A launch file is something that will launch multiple nodes in ROS, to use a launch file run the following command:

.. code-block:: bash

    ros2 launch <package-name> <launch-file>.py

Launch files will be covered in class.

ROS2 Setting Parameters
^^^^^^^^^^^^^^^^^^^^^^^

Sometimes a Node will have parameters associated with it. Consider parameters as variables that you can set for your when starting them up or during the process of running the node.
This removes the requirement of building the workspace again. parameters can be set as follows:

.. code-block:: bash

    ros2 param set <node-name> <parameter-name> <value>

Sometimes the node name will be replaced by the name field in launch files. Parameters can be listed using,

.. code-block:: bash

    ros2 param list

You can get the current value of a parameter using,

.. code-block:: bash
     
    ros2 param get <node-name> <parameter-name>

Building a Workspace
^^^^^^^^^^^^^^^^^^^^

To run a custom package that is written you will have to first build the workspace. To do this execute the following:

.. code-block:: bash

    colcon build

You can also build singular packages using this command

.. code-block:: bash

    colcon build --packages-select <pkg_name>

This will essentially just copy your files over to the ``build`` , ``install`` , and ``log`` directories. Then you can source your local workspace by executing the following:

.. code-block:: bash

    . install/setup.bash

or

.. code-block:: bash

    source install/setup.bash


Git
---

First you must ensure you have Git installed on your computer. If you haven't, installation instructions are available at the `Installation <installation.html>`_ page.

Clone a Repo
^^^^^^^^^^^^
The following command will clone a repo into the working directory you are in.

.. code-block:: bash

    git clone <repo-url>

The clone command will clone the repo into a directory with the repo name. To clone a branch within a repo, the following can be used.

.. code-block:: bash

    git clone --branch <branch-name> <repo-url>

.. note:: ``<stuff>`` means you remove the entire thing and replace it with a single url, name or something else based on what you want to do.

Changing to a Different Branch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To change to a different branch in your local repo you can do the following:

.. code-block:: bash

    git checkout <branch-name>

this will change your active branch. To check which branch you are on you can run the following:

.. code-block:: bash

    git branch

Adding to your Remote Repo After Cloning 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To add or stage changes that you have made inside your local repo, run the following command.

.. code-block:: bash

    git add .

This will stage all changes. If you want to stage specific changes, run the following command.

.. code-block:: bash

    git add <path-to-file>

That will stage changes in a certain directory or a certain file that was changed. After that you need to commit your changes that can be done with the following command.

.. code-block:: bash

    git commit -m "Message regarding your changes"

This will commit your changes and now they are ready for synchronization to your remote repo. That can be done with the following command.

.. code-block:: bash

    git push

This will push your changes. To pull any new changes done, do the following.

.. code-block:: bash

    git pull

To merge a branch with the main branch, you can run the following commands.

.. code-block:: bash

    git checkout <name-of-main-branch>
    git merge orgin/<name-of-branch>
    git push

This is will help with collaboration there are a lot of resources for git online, I would check them out.

Collaboration
^^^^^^^^^^^^^

To collaborate on a project, create branches once you have edited a local repo. Try not to push to the main. Edit, test, review and then merge to main. To change and create a new branch simultaneously run the following command:

.. code-block:: bash

    git checkout -b <branch-name>

Now you are in a new branch. Now add and commit your changes. Then to push, run the following command:

.. code-block:: bash

    git push --set-upstream origin <branch-name>

Then up on GitHub or GitLab, create a pull request to merge to your main branch, when your team is satisfied with your code.

TMUX
----

TMUX is a useful tool to use when working with SSH or even in general. TMUX allows you to split up your terminal into different terminals inside your current terminal without having to open new windows.
By now you should know how to install tmux using the ``apt`` package manager.

Once installed you can run it using the following:

.. code-block:: bash

    tmux

To do any tmux command you must first hit ``Ctrl`` + ``b`` (which is commonly referred to as ``Leader``), release it, then use whatever other command you need to do. 

To split your terminal vertically you can do ``Leader``, release it, then hit ``%``. To split a terminal window horizontally do ``Leader`` ``"``. To move between the terminal blocks use ``Leader`` and then the arrow keys.
To exit out of the split up terminals, just type exit in each terminal, and it will close you out of tmux. You can also use ``Leader`` ``x`` to prompt to  close an individual pane (a single terminal prompt). This can be very helpful when a command is stuck.

A more complete cheat sheet can be found at `this link <https://tmuxcheatsheet.com/>`_

If you want your terminal prompt to be colored in inside tmux, you can add a file called .tmux.conf to your home directory

.. code-block:: bash

    echo set -g default-terminal \"screen-256color\" >> ~/.tmux.conf

