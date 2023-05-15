#!/usr/bin/env python3
"""
Author: Wes Henderson
Control your lights with the unofficial LIFX CLI. This CLI uses the
LIFX HTTP endpoints to configure your lights.
https://api.developer.lifx.com/reference/introduction
"""
import argparse
from src.lifx.auth import Auth
from src.lifx.colors import Colors
from src.lifx.lights import Lights
from src.lifx.scenes import Scenes

auth = Auth()
colors = Colors()
light = Lights()
scene = Scenes()

LOGO = """
██      ██ ███████ ██   ██      ██████ ██      ██
██      ██ ██       ██ ██      ██      ██      ██
██      ██ █████     ███       ██      ██      ██
██      ██ ██       ██ ██      ██      ██      ██
███████ ██ ██      ██   ██      ██████ ███████ ██

"""


def lights_sub_command(args):
    """Control the actions for the 'lights' sub-command."""
    devices = args.list_devices
    light_id = args.light_id
    toggle = args.toggle
    group = args.group
    state = args.state
    color = args.color
    power = args.power
    brightness = args.brightness
    infrared = args.infrared
    duration = args.duration

    if devices:
        light.get()

    if toggle:
        light.toggle(light_id, group)

    if state:
        state_attributes = {'power': power,
                            'brightness': brightness,
                            'duration': duration,
                            'infrared': infrared}
        light.set_state(light_id, group, color, state_attributes)


def scenes_sub_command(args):
    """Control the actions for the 'scenes' sub-command."""
    scenes = args.list_scenes
    scene_id = args.scene_id

    if scenes:
        scene.get()

    if scene_id:
        scene.activate(scene_id)


def effects_sub_command(args):
    """Control the actions for the 'effects' sub-command."""
    list_effects = args.list_effects
    light_id = args.light_id
    group = args.group
    color = args.color
    breathe = args.breathe
    pulse = args.pulse
    stop = args.stop

    if list_effects:
        light.list_effects()
    if breathe:
        light.breathe_effect(light_id, group, color)
    elif pulse:
        light.pulse_effect(light_id, group, color)
    elif stop:
        light.stop_effect(light_id, group)


def colors_sub_command(args):
    """Control the actions for the 'colors' sub-command."""
    list_colors = args.list_colors
    provided_color = args.colors

    if list_colors:
        colors.color_information()

    if provided_color:
        colors.validate_color(provided_color)


def main():
    """Main entrypoint for the LIFX CLI."""
    print(LOGO)
    # Create the parser
    description = 'Control LIFX devices via the CLI!'
    epilog = 'Run `lifx --configure` to setup authentication.'
    job_options = argparse.ArgumentParser(description=description, epilog=epilog)

    # Add the arguments
    job_options.add_argument('-c',
                             '--configure',
                             default=False,
                             action='store_true',
                             help='Add your LIFX token to the local authentication file: ~/.keys')

    # Add the 'lights' sub-command.
    light_job_options = job_options.add_subparsers(dest='command')
    light_command = light_job_options.add_parser('lights', help='Light specific functions.')
    light_command.add_argument('-l',
                               '--list',
                               default=False,
                               dest='list_devices',
                               action='store_true',
                               help='List LIFX devices.')
    light_command.add_argument('-i',
                               '--id',
                               default=False,
                               dest='light_id',
                               action='store',
                               metavar='ID',
                               help='Specify the light ID.')
    light_command.add_argument('-t',
                               '--toggle',
                               default=False,
                               dest='toggle',
                               action='store_true',
                               help='Toggle the specified light.')
    light_command.add_argument('-g',
                               '--group',
                               default=False,
                               dest='group',
                               action='store_true',
                               help='Specify whether or not the target is a group.')
    light_command.add_argument('-s',
                               '--state',
                               default=False,
                               action='store_true',
                               help='Set the state for the specified light.')
    light_command.add_argument('-c',
                               '--color',
                               default='green',
                               action='store',
                               help='Use the specified color. [Default: green]')
    light_command.add_argument('-p',
                               '--power',
                               default='on',
                               action='store',
                               help='State: on or off [Default: on]')
    light_command.add_argument('-b',
                               '--brightness',
                               default=0.5,
                               action='store',
                               help='State: 0.0 to 1.0 [Default: 0.5]')
    light_command.add_argument('-r',
                               '--infrared',
                               default=0.5,
                               action='store',
                               help='State: 0.0 to 1.0 [Default: 1.0]')
    light_command.add_argument('-u',
                               '--duration',
                               default=1,
                               action='store',
                               help='State: How many seconds should the action take. [Default: 1]')

    # Add the 'scenes' sub-command.
    scene_command = light_job_options.add_parser('scenes', help='Scene specific functions.')
    scene_command.add_argument('-l',
                               '--list',
                               default=False,
                               dest='list_scenes',
                               action='store_true',
                               help='List LIFX scenes.')
    scene_command.add_argument('-i',
                               '--id',
                               default=False,
                               dest='scene_id',
                               action='store',
                               metavar='ID',
                               help='Activate scene.')

    # Add the 'effects' sub-command.
    effects_description = 'Control lighting effects.'
    effects_epilog = "Note: The CLI can only control effects stored on your light's firmware."
    effects_help = 'Effects specific functions.'
    effect_command = light_job_options.add_parser('effects', description=effects_description,
                                                  epilog=effects_epilog, help=effects_help)
    effect_command.add_argument('-l',
                                '--list',
                                default=False,
                                dest='list_effects',
                                action='store_true',
                                help='List effects supported by the LIFX CLI.')
    effect_command.add_argument('-i',
                                '--id',
                                default=False,
                                dest='light_id',
                                action='store',
                                metavar='ID',
                                help='Specify the light ID.')
    effect_command.add_argument('-g',
                                '--group',
                                default=False,
                                action='store_true',
                                help='Specify whether or not the target is a group.')
    effect_command.add_argument('-c',
                                '--color',
                                default=[],
                                action='append',
                                help='Specify the color; multiple -c options alternate colors.')
    effect_command.add_argument('--breathe',
                                default=False,
                                action='store_true',
                                help='Effects: Breathe')
    effect_command.add_argument('--pulse',
                                default=False,
                                action='store_true',
                                help='Effects: Pulse')
    effect_command.add_argument('--stop',
                                default=False,
                                action='store_true',
                                help='Effects: Stop')

    # Add the 'Colors' sub-command.
    colors_description = 'Explore all of the color-related options!'
    colors_help = 'Learn how to provide colors to the CLI.'
    color_command = light_job_options.add_parser('colors', description=colors_description,
                                                 help=colors_help)
    color_command.add_argument('-l',
                               '--list',
                               default=False,
                               dest='list_colors',
                               action='store_true',
                               help='List color options supported by the LIFX CLI.')
    color_command.add_argument('-c',
                               '--color',
                               default=False,
                               dest='colors',
                               action='store',
                               help='Validate a color using the LIFX API.')

    args = job_options.parse_args()
    configure = args.configure

    # Configure authentication.
    if configure:
        auth.configure()

    # The 'lights' sub-command.
    if args.command == 'lights':
        lights_sub_command(args)

    # The 'scenes' sub-command.
    if args.command == 'scenes':
        scenes_sub_command(args)

    # The 'effects' sub-command.
    if args.command == 'effects':
        effects_sub_command(args)

    # The 'colors' sub-command.
    if args.command == 'colors':
        colors_sub_command(args)


if __name__ == '__main__':
    main()
