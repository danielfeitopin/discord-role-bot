# Discord bot that assigns roles using slash commands

## Contents

Python code snippet with the code needed to give a Discord bot the functionality to add roles to the user who invoked the slash command.

## Usage

1. Assign the bot's Token to the constant TOKEN.
2. Add the IDs of the Discord servers on which the bot will act to GUILD_IDS (list of int).
3. Add as many `create_choice` as needed with their `name` and `value` parameters.

## Comments

- Only the functionality of **adding roles** is included. To **remove roles**, a similar function would be used by modifying the messages and replacing the `add_roles` method (line 53) with the `remove_roles` method.
- For the command to work:
  - The bot must have the `Manage Roles` permission on the server.
  - The bot must have a role superior to the roles it handles.
- It is recommended to have some control over who uses the command.

## Requirements

- `discord.py`
- `discord-py-slash-command`

## Reference

- <https://discordpy.readthedocs.io/>
- <https://discord-py-slash-command.readthedocs.io/>
