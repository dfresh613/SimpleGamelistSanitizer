# Simple Gamelist Sanitizer

Simply and easily run a single script to parse thorough an existing EmulationStation
gamelist to sanitize and remove any vulgar, casino, mahjong, duplicate or other known unusable games from the gamelist.
Primarily for arcade gameslist
 
## Installation
pip3 install sgsanitizer

## Usage
`sgsanitizer <gamelist.xml> <output_file>`

## help
```
 sgsanitizer -h
 usage: sgsanitizer [-h] gamelist_path output_file

 Provide a gamelist.xml file and it will do its best to sanitize and removeany
 vulgar, casino, mahjong, or other known unusable games from the gamelist.
 Primarily for arcade games

 positional arguments:
   gamelist_path  full path to gamelist.xml
   output_file    full path to output location
```
