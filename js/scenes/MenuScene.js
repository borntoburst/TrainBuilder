/*
=====================================================
 TrainBuilder
 Menu Scene
=====================================================
*/

export class MenuScene extends Phaser.Scene {

    constructor() {

        super("MenuScene");

    }

    create() {

        // =====================================================
        // Background
        // =====================================================

        this.cameras.main.setBackgroundColor("#87CEEB");

        // =====================================================
        // Title
        // =====================================================

        this.add.text(
            640,
            150,
            "TRAINBUILDER",
            {
                fontFamily: "Arial",
                fontSize: "56px",
                color: "#222222",
                fontStyle: "bold"
            }
        ).setOrigin(0.5);

        // =====================================================
        // Start Button
        // =====================================================

        const startButton = this.add.text(
            640,
            330,
            "BẮT ĐẦU",
            {
                fontFamily: "Arial",
                fontSize: "36px",
                backgroundColor: "#4CAF50",
                color: "#FFFFFF",
                padding: {
                    left: 30,
                    right: 30,
                    top: 15,
                    bottom: 15
                }
            }
        )
        .setOrigin(0.5)
        .setInteractive({ useHandCursor: true });

        startButton.on("pointerdown", () => {

            this.scene.start("GameplayScene");

        });

        // =====================================================
        // Config Button
        // =====================================================

        const configButton = this.add.text(
            640,
            430,
            "CÀI ĐẶT",
            {
                fontFamily: "Arial",
                fontSize: "36px",
                backgroundColor: "#1976D2",
                color: "#FFFFFF",
                padding: {
                    left: 30,
                    right: 30,
                    top: 15,
                    bottom: 15
                }
            }
        )
        .setOrigin(0.5)
        .setInteractive({ useHandCursor: true });

        configButton.on("pointerdown", () => {

            this.scene.start("ConfigScene");

        });

    }

}
