# coding: utf-8
from __future__ import unicode_literals
import os


smileys_base = {
    "smile.png": (":)", ":-)", ),
    "heureux.png": (":D", ":-D", ),
    "clin.png": (";)", ";-)", ),
    "langue.png": (":p", ":P", ":-p", ":-P", ),
    "rire.gif": (":lol:", ),
    "unsure.gif": (":euh:", ),
    "triste.png": (":(", ":-(", ),
    "huh.png": (":o", ":-o", ":O", ":-O", ),
    "mechant.png": (":colere2:", ),
    "blink.gif": ("o_O", "O_o", ),
    "hihi.png": ("^^", ),
    "siffle.png": (":-°", ":°", ),
    "ange.png": (":ange:", ),
    "angry.gif": (":colere:", ),
    "diable.png": (":diable:", ),
    "magicien.png": (":magicien:", ),
    "ninja.png": (":ninja:", ),
    "pinch.png": (">_<", ),
    "pirate.png": (":pirate:", ),
    "pleure.png": (":'(", ),
    "rouge.png": (":honte:", ),
    "soleil.png": (":soleil:", ),
    "waw.png": (":waw:", ),
    "zorro.png": (":zorro:", ),
    "cthulhu.png": ("^(;,;)^", ),
}


def markdown(settings, conf):
    base_path = os.path.join(settings["template_path"], "smileys")
    return "\n".join(u"*![{}]({})".format(s, os.path.join(base_path, fn)) for fn, ls in smileys_base.items() for s in ls)
    
