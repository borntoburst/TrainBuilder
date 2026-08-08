/*
=====================================================
 TrainBuilder
 Gameplay Scene
=====================================================
*/

export class GameplayScene extends Phaser.Scene {

    constructor() {

        super("GameplayScene");

    }

    create() {

        // =====================================================
        // Background
        // =====================================================

        this.cameras.main.setBackgroundColor("#DCEEFF");

        // =====================================================
        // Title
        // =====================================================

        this.add.text(
            640,
            70,
            "GAMEPLAY",
            {
                fontFamily: "Arial",
                fontSize: "48px",
                color: "#222222",
                fontStyle: "bold"
            }
        ).setOrigin(0.5);

        // =====================================================
        // Placeholder
        // =====================================================

        this.add.text(
            640,
            360,
            "Gameplay Scene\n(Coming Soon)",
            {
                fontFamily: "Arial",
                fontSize: "30px",
                color: "#555555",
                align: "center"
            }
        ).setOrigin(0.5);

        // =====================================================
        // Back Button
        // =====================================================

        const backButton = this.add.text(
            640,
            620,
            "VỀ MENU",
            {
                fontFamily: "Arial",
                fontSize: "32px",
                backgroundColor: "#607D8B",
                color: "#FFFFFF",
                padding: {
                    left: 24,
                    right: 24,
                    top: 12,
                    bottom: 12
                }
            }
        )
        .setOrigin(0.5)
        .setInteractive({ useHandCursor: true });

        backButton.on("pointerdown", () => {

            this.scene.start("MenuScene");

        });

    }

}
