/*
=====================================================
 TrainBuilder
 Game
=====================================================
*/

import { GAME_CONFIG } from "./config.js";

export class Game {

    constructor() {

        this.instance = null;

    }

    start() {

        if (this.instance) {
            return;
        }

        this.instance = new Phaser.Game(GAME_CONFIG);

    }

}
