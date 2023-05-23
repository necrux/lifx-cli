#!/usr/bin/env python3
"""Tests for lifx-cli."""
import pytest
import src.lifx.lifx
from src.lifx.auth import Auth
from src.lifx.colors import Colors
from src.lifx.effects import Effects
from src.lifx.lights import Lights
from src.lifx.scenes import Scenes

VERSION = "2.5.4"
TEST_HELP = "Control LIFX devices via the CLI!"
TEST_GROUP = "68931117c352834e0a8f70aebcbcdae1"
TEST_COLORS = ["purple", "green"]
TEST_CYCLES = 4
TEST_LIGHT = "d073d568d053"
TEST_SCENE = "9371a59c-6ee7-4ced-a3d3-b25d9fc08aad"

auth = Auth()
colors = Colors()
effects = Effects()
lights = Lights()
scenes = Scenes()


@pytest.mark.parametrize("option", ("-v", "--version"))
def test_version(capsys, option):
    """Test the version output."""
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        src.lifx.lifx.main([option])
    out, err = capsys.readouterr()
    assert f"Version: {VERSION}" in out
    assert err == ""
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0


@pytest.mark.parametrize("option", ("-h", "--help"))
def test_help(capsys, option):
    """Test the help output."""
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        src.lifx.lifx.main([option])
    out, err = capsys.readouterr()
    assert TEST_HELP in out
    assert err == ""
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0


def test_auth():
    """Validate the API token."""
    assert auth.validate_token()


def test_colors(capsys):
    """Test the colors sub-command."""
    colors.validate_color(color="blue")
    out, err = capsys.readouterr()
    assert "Saturation" in out
    assert err == ""


def test_effects():
    """Test the effects sub-command (lights will flash at Wes' home)."""
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        effects.breathe_effect(light_id=TEST_GROUP, group=True,
                               color=TEST_COLORS, cycles=TEST_CYCLES)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0


def test_lights(capsys):
    """Test the lights sub-command."""
    lights.get()
    out, err = capsys.readouterr()
    assert TEST_LIGHT in out
    assert err == ""


def test_scenes(capsys):
    """Test the scenes sub-command."""
    scenes.get()
    out, err = capsys.readouterr()
    assert TEST_SCENE in out
    assert err == ""
