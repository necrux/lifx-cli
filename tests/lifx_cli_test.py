#!/usr/bin/env python3
import pytest
import src.lifx.lifx


def test_colors(capsys):
    cli_args = [False, 'blue']
    src.lifx.lifx.colors_sub_command(cli_args)
    out, err = capsys.readouterr()
    assert "Saturation" in out
    assert err == ""


def test_effects(capsys):
    cli_args = [False, '917e85258fa3c3fe15816a04db6a9a15', True, ['purple'], True, False, False]
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        src.lifx.lifx.effects_sub_command(cli_args)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0


def test_lights(capsys):
    cli_args = [True, False, False, False, False, False, False, False, False, False]
    src.lifx.lifx.lights_sub_command(cli_args)
    out, err = capsys.readouterr()
    assert "d073d568d053" in out
    assert err == ""


def test_scenes(capsys):
    cli_args = [True, False]
    src.lifx.lifx.scenes_sub_command(cli_args)
    out, err = capsys.readouterr()
    assert "9371a59c-6ee7-4ced-a3d3-b25d9fc08aad" in out
    assert err == ""
