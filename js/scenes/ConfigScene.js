/*
=====================================================
 TrainBuilder
 Config Scene
=====================================================
*/

export class ConfigScene extends Phaser.Scene {

    constructor() {

        super("ConfigScene");

    }

    create() {

        // =====================================================
        // Background
        // =====================================================

        this.cameras.main.setBackgroundColor("#F5F5F5");

        // =====================================================
        // Title
        // =====================================================

        this.add.text(
            640,
            120,
            "CÀI ĐẶT",
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
            "Teacher Configuration\n(Coming Soon)",
            {
                fontFamily: "Arial",
                fontSize: "28px",
                color: "#555555",
                align: "center"
            }
        ).setOrigin(0.5);

        // =====================================================
        // Back Button
        // =====================================================

        const backButton = this.add.text(
            640,
            600,
            "QUAY LẠI",
            {
                fontFamily: "Arial",
                fontSize: "34px",
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

        backButton.on("pointerdown", () => {

            this.scene.start("MenuScene");

        });

    }

}
