/*
=====================================================
 TrainBuilder
 Boot Scene
=====================================================
*/

export class BootScene extends Phaser.Scene {

    constructor() {

        super("BootScene");

    }

    preload() {

        /*
        =====================================================
        Train
        =====================================================
        */

        this.load.image(
            "train_engine",
            "assets/train/engine/train_engine.png"
        );

        this.load.image(
            "wagon_empty",
            "assets/train/wagons/wagon_empty.png"
        );

        /*
        =====================================================
        Track
        =====================================================
        */

        this.load.image(
            "track_straight",
            "assets/train/track/track_straight.png"
        );

        /*
        =====================================================
        Background
        =====================================================
        */

        this.load.image(
            "gameplay_background",
            "assets/backgrounds/gameplay/gameplay_background.png"
        );

        /*
        =====================================================
        UI
        =====================================================
        */

        this.load.image(
            "question_panel",
            "assets/ui/question_panel.png"
        );

        this.load.image(
            "building_slot",
            "assets/ui/building_slot.png"
        );

        /*
        =====================================================
        Particles
        =====================================================
        */

        this.load.image(
            "smoke",
            "assets/particles/smoke.png"
        );

        this.load.image(
            "sparkle",
            "assets/particles/sparkle.png"
        );

    }

    create() {

        this.scene.start("MenuScene");

    }

}
