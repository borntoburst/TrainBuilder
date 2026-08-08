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
        Backgrounds
        =====================================================
        */

        this.load.setPath("assets");

        // Ví dụ:
        // this.load.image("menu_background", "backgrounds/menu.png");
        // this.load.image("gameplay_background", "backgrounds/gameplay.png");

    }

    create() {

        this.scene.start("MenuScene");

    }

}
