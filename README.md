# Convert .Net Resource File (.resx) to iOS/Android translation file (.strings / .xml)
This Python based command tool helps to generate translation string files for iOS(.strings) and Android(string.xml) native projects from .resx file which is .Net resource file used in Xamarin/.Net applications. Usually we need to put tedious effort and time to extract the key and translation data meticulously to convert them into platform supported format. This tool will help to achieve the same job in short time with high accuracy.

#### Sample .resx File
```xml
<resources>
  <data name="print_successful_message">
      <value>Printing has been completed successfully.</value>
      <comment>This message is displayed to intimate print successful status</comment>
  </data>
  <data name="user_welcome_message">
      <value>Welcome!</value>
      <comment>This message is displayed when user landed on the screen after login.</comment>
  </data>
</resources>
```
#### Localization.strings file for iOS native project
```xml

"print_successful_message" = "Printing has been completed successfully."
"user_welcome_message" = "Welcome!"
```
#### strings.xml file for Android native project
```xml

<resources>
  <string name="print_successful_message">Printing has been completed successfully.</string>
  <string name="user_welcome_message">Welcome!</string>
</resources>
```

#### Tool Commandline Arguments
``Supported arguments: ResxToPlatfromStringConverter.py  [-idir input directory]
                                           [-iextension input files format optional] 
                                           [-odir output directory]
                                           [-platform platform ios|android] 
                                           [-log True/False to enable display process logs]
                                        ``
#### Tool Usage

`python3 ResxToPlatfromStringConverter.py -idir "/path/to/ResxfilesDirectory" -odir "/path/to/OutputDirectory" -platform "ios"`
