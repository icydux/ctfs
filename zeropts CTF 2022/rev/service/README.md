We are given a ``PE32+ executable (console) x86-64`` file.

The first thing that I did, was to run the executable. It asks for a flag(input) in the console and then the process terminates.

![Screenshot](screenshots/console.PNG)

Next, I loaded the executable to ``Cutter`` and identified the offset that the input is parsed based on the ``ReadConsoleA`` import.


