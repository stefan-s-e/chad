'''
chad, an idiosyncratic CLI time-tracking software written by hand.
Copyright (C) 2026, Stefan Stealey-Euchner (stefan.stealey.euchner@gmail.com)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import json
import shutil
import os
from datetime import datetime

def main():
    PrintMainMenu()
    TakeUserInput()

def PrintMainMenu():
    print(f"\nWelcome to chad! You're using version TODO.\n")

def TakeUserInput():
    allowedCommands = ['m', 'q', 'p', 'j', 'r']

    print("Command (m for help): ", end='')
    userInput = input()

    if (len(userInput) != 1 or userInput not in allowedCommands):
        print(f"Invalid command. Please use m for help.")
        TakeUserInput()

    HandleCommand(userInput)

def HandleCommand(command):
    match command:
        case 'm':
            HandleMenu()
        case 'q':
            HandleQuit()
        case 'p':
            HandlePunch()
        case 'j':
            HandleJiraLog()
        case 'r':
            HandleReport()

    TakeUserInput()

def HandleMenu():
    print("\nHelp:")
    print("m    print this menu")
    print("q    quit chad")
    print("p    punch in/out")
    print("j    log jira hours")
    print("r    generate report\n")

def HandleQuit():
    quit()

def HandlePunch():
    UpdateBackup()
    existing_data = {}

    with open("db.json", mode="r", encoding="utf-8") as db_file:
        existing_data = json.load(db_file)

    existing_data["punches"].append(str(datetime.now().replace(second=0, microsecond=0)))

    with open("db.json", mode="w", encoding="utf-8") as db_file:
        json.dump(existing_data, db_file)

    print(f"Punch recorded at time {str(datetime.now().replace(second=0, microsecond=0))}\n")

def HandleJiraLog():
    UpdateBackup()
    print("Hours logged: ", end='')
    userInput = input()
    try:
        float_userInput = float(userInput)
    except:
        print(f"Invalid value. Please enter a number.")
        HandleJiraLog()
        return

    existing_data = {}
    currDayString = str(datetime.now().date())

    with open("db.json", mode="r", encoding="utf-8") as db_file:
        existing_data = json.load(db_file)

    existing_data["jira_logs"][currDayString] = existing_data["jira_logs"].get(currDayString, 0) + float_userInput

    with open("db.json", mode="w", encoding="utf-8") as db_file:
        json.dump(existing_data, db_file)

    print(f"{float_userInput} Jira hours recorded on {str(datetime.now().date())}\n")

def HandleReport():
    existing_data = {}

    with open("db.json", mode="r", encoding="utf-8") as db_file:
        existing_data = json.load(db_file)
    
    allHoursWorked = computeHoursWorked(existing_data["punches"])
    allJiraHoursLogged = computeJiraHoursLogged(existing_data["jira_logs"])

    print(f"Hours worked (all time): {allHoursWorked}")
    print(f"Jira hours logged (all time): {allJiraHoursLogged}\n")

def computeHoursWorked(dateTimeStringList):
    deltaList = list(map(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"), dateTimeStringList))
    return sum(
        map(
            lambda x: x.seconds / 3600, 
            [item2 - item1 for item1, item2 in zip(deltaList[::2], deltaList[1::2])]
        )
    )

def computeJiraHoursLogged(jiraDictList):
    return sum(jiraDictList.values())

def UpdateBackup():
    shutil.copy("db.json", "db_backup.json")

if __name__ == "__main__":
    main()