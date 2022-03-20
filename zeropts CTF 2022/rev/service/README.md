We are given a ``PE32+ executable (console) x86-64`` file.

The first thing that I did, was to run the executable. It asks for a flag(input) in the console and then the process terminates.

![Screenshot](screenshots/console.PNG)

Next, I loaded the executable to ``Cutter`` and identified the offset that the input is read based on the ``ReadConsoleA`` import.

![Screenshot](screenshots/main.PNG)

The input is stored at ``rbp-0x60`` and the offset address is passed as an argument to the function ``fcn.00401550``.
