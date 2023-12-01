# Core components

## Subsections: [Windows kernel](#windows-kernel-windows-nt) - [Core processes](#core-processes-windows-nt) - [System startup](#system-startup-windows-nt) - [Graphical subsystem](#graphical-subsystem)


### Windows kernel (Windows NT) [⌂](#core-components)
|Component|Description|Open Replacement|
|:-:|:-:|:-:|
|[Ntoskrnl.exe](https://en.wikipedia.org/wiki/Ntoskrnl.exe)|Provides the kernel and executive layers of the kernel architecture, and is responsible for services such as hardware virtualization, process and memory management, etc.|[Windows Research Kernel](https://github.com/zhuhuibeishadiao/ntoskrnl)|
|[hal.dll](https://en.wikipedia.org/wiki/Hal.dll)|Provides and handles the interaction between software and hardware via the Hardware Abstraction Layer||
|[kernel32.dll](https://en.wikipedia.org/wiki/Kernel32.dll)|Provides kernel operations to apps in the Win32 mode, like memory management, I/Os, process creation, etc.||


### Core processes (Windows NT) [⌂](#core-components)
|Component|Description|Open Replacement|
|:-:|:-:|:-:|
|[System idle process](https://en.wikipedia.org/wiki/System_idle_process)|A counter which measures how much idle capacity the CPU has at any given time||
|[Session Manager Subsystem](https://en.wikipedia.org/wiki/Session_Manager_Subsystem)|Performs several critical boot-time operations, such as the creation of environment variables, starting CSRSS, and performing file-copy operations that were queued up from before the system was booted (pending file rename operations)||
|[Client/Server Runtime Subsystem](https://en.wikipedia.org/wiki/Client/Server_Runtime_Subsystem)|Provides the capability for applications to use the [Windows API](https://en.wikipedia.org/wiki/Windows_API)||
|[Local Security Authority Subsystem Service](https://en.wikipedia.org/wiki/Local_Security_Authority_Subsystem_Service)|Verifies users logging on to the computer and creates security tokens||
|[Winlogon](https://en.wikipedia.org/wiki/Winlogon)|Responsible for handling the secure attention key, loading the user profile on logon, and optionally locking the computer when a screensaver is running||
|[Svchost.exe](https://en.wikipedia.org/wiki/Svchost.exe)|A generic host process name for services that run from dynamic-link libraries (DLLs)||
|[Windows on Windows](https://en.wikipedia.org/wiki/Windows_on_Windows) and [WOW64](https://en.wikipedia.org/wiki/WOW64)|An abstraction layer that allows legacy code to operate on more modern versions of Windows||
|[Virtual DOS machine](https://en.wikipedia.org/wiki/Virtual_DOS_machine)|Allows MS-DOS apps to run on Intel 80386 or higher computers when there is already another operating system running and controlling the hardware|[WineVDM](https://github.com/otya128/winevdm)|

## System startup (Windows NT) [⌂](#core-components)
|Component|Description|Open Replacement|
|:-:|:-:|:-:|
|[NTLDR](https://en.wikipedia.org/wiki/NTLDR), IA64ldr, [Winload](https://en.wikipedia.org/wiki/Winload.exe)|Performs basic system initialization options such as loading the hardware abstraction layer and boot-time device drivers, prior to passing control to the Windows kernel||
|[Recovery Console](https://en.wikipedia.org/wiki/Recovery_Console)|Provides the means for administrators to perform a limited range of tasks using a command line interface, primarily to aid in recovering from situations where Windows does not boot successfully||
|[ntdetect.com](https://en.wikipedia.org/wiki/Ntdetect.com)|Used during the boot process to detect basic hardware components that may be required during the boot process||
|[Windows Boot Manager](https://en.wikipedia.org/wiki/Windows_Boot_Manager)|Displays boot menus to the user if multiple operating systems are configured in the system's Boot Configuration Data||

## Graphical subsystem [⌂](#core-components)
|Component|Description|Open Replacement|
|:-:|:-:|:-:|
|[Desktop Window Manager](https://en.wikipedia.org/wiki/Desktop_Window_Manager)|Handles compositing and manages special effects on screen objects in a graphical user interface||
|[Graphics Device Interface](https://en.wikipedia.org/wiki/Graphics_Device_Interface)|Representing graphical objects and transmitting them to output devices such as monitors and printers|[GDIPP](https://github.com/CoolOppo/GDIPP) / [libgdiplus](https://github.com/mono/libgdiplus)|
|[Windows USER](https://en.wikipedia.org/wiki/Windows_USER)|Provides core user interface, messaging and visual elements||
