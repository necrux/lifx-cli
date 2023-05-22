#!/usr/bin/env python3
"""Tests for lifx-cli."""
import pytest
import src.lifx.lifx


def test_colors(capsys):
    """Test the colors sub-command."""
    cli_args = [False, 'blue']
    src.lifx.lifx.colors_sub_command(cli_args)
    out, err = capsys.readouterr()
    assert "Saturation" in out
    assert err == ""


def test_effects():
    """Test the effects sub-command (lights will flash purple as Wes' home)."""
    cli_args = [False, '68931117c352834e0a8f70aebcbcdae1', True, ['purple'], 4, True, False, False]
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        src.lifx.lifx.effects_sub_command(cli_args)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0


def test_lights(capsys):
    """Test the lights sub-command."""
    cli_args = [True, False, False, False, False, False, False, False, False, False, False]
    src.lifx.lifx.lights_sub_command(cli_args)
    out, err = capsys.readouterr()
    assert "d073d568d053" in out
    assert err == ""


def test_scenes(capsys):
    """Test the scenes sub-command."""
    cli_args = [True, False]
    src.lifx.lifx.scenes_sub_command(cli_args)
    out, err = capsys.readouterr()
    assert "9371a59c-6ee7-4ced-a3d3-b25d9fc08aad" in out
    assert err == ""
