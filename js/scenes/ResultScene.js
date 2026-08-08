/*
=====================================================
 TrainBuilder
 Result Scene
=====================================================
*/

export class ResultScene extends Phaser.Scene {

    constructor() {

        super("ResultScene");

    }

    create() {

        // =====================================================
        // Background
        // =====================================================

        this.cameras.main.setBackgroundColor("#FFF8DC");

        // =====================================================
        // Title
        // =====================================================

        this.add.text(
            640,
            120,
            "HOÀN THÀNH!",
            {
                fontFamily: "Arial",
                fontSize: "52px",
                color: "#222222",
                fontStyle: "bold"
            }
        ).setOrigin(0.5);

        // =====================================================
        // Placeholder
        // =====================================================

        this.add.text(
            640,
            260,
            "Result Scene\n(Coming Soon)",
            {
                fontFamily: "Arial",
                fontSize: "28px",
                color: "#555555",
                align: "center"
            }
        ).setOrigin(0.5);

        // =====================================================
        // Play Again Button
        // =====================================================

        const playAgainButton = this.add.text(
            640,
            430,
            "CHƠI LẠI",
            {
                fontFamily: "Arial",
                fontSize: "32px",
                backgroundColor: "#4CAF50",
                color: "#FFFFFF",
                padding: {
                    left: 28,
                    right: 28,
                    top: 14,
                    bottom: 14
                }
            }
        )
        .setOrigin(0.5)
        .setInteractive({ useHandCursor: true });

        playAgainButton.on("pointerdown", () => {

            this.scene.start("GameplayScene");

        });

        // =====================================================
        // Menu Button
        // =====================================================

        const menuButton = this.add.text(
            640,
            530,
            "VỀ MENU",
            {
                fontFamily: "Arial",
                fontSize: "32px",
                backgroundColor: "#607D8B",
                color: "#FFFFFF",
                padding: {
                    left: 28,
                    right: 28,
                    top: 14,
                    bottom: 14
                }
            }
        )
        .setOrigin(0.5)
        .setInteractive({ useHandCursor: true });

        menuButton.on("pointerdown", () => {

            this.scene.start("MenuScene");

        });

    }

}
