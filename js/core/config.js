/*
=====================================================
 TrainBuilder
 Game Configuration
=====================================================
*/

import { BootScene } from "../scenes/BootScene.js";
import { MenuScene } from "../scenes/MenuScene.js";
import { ConfigScene } from "../scenes/ConfigScene.js";
import { GameplayScene } from "../scenes/GameplayScene.js";
import { ResultScene } from "../scenes/ResultScene.js";

export const GAME_CONFIG = {

    type: Phaser.AUTO,

    parent: "game-container",

    width: 1280,

    height: 720,

    backgroundColor: "#87CEEB",

    fps: {
        target: 60,
        forceSetTimeOut: true
    },

    scale: {

        mode: Phaser.Scale.FIT,

        autoCenter: Phaser.Scale.CENTER_BOTH

    },

    scene: [

        BootScene,

        MenuScene,

        ConfigScene,

        GameplayScene,

        ResultScene

    ]

};
