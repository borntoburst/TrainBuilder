/*
=====================================================
 TrainBuilder
 Gameplay Scene
=====================================================
*/

import { TrainSystem } from "../systems/TrainSystem.js";

export class GameplayScene extends Phaser.Scene {

    constructor() {

        super("GameplayScene");

        this.trainSystem = null;

    }

    create() {

        // =====================================================
        // Background
        // =====================================================

        this.cameras.main.setBackgroundColor("#DCEEFF");

        // Nếu đã có background thì bỏ comment dòng dưới
        // this.add.image(640, 360, "gameplay_background");

        // =====================================================
        // Train
        // =====================================================

        this.trainSystem = new TrainSystem(this);

        this.trainSystem.create();

    }

    update(time, delta) {

        if (this.trainSystem) {

            this.trainSystem.update(delta);

        }

    }

}
