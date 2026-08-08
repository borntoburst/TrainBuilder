/*
=====================================================
 TrainBuilder
 Train System
=====================================================
*/

export class TrainSystem {

    constructor(scene) {

        this.scene = scene;

        this.engine = null;

        this.wagons = [];

        this.wagonCount = 3;

        this.wagonSpacing = 140;

    }

    // =====================================================
    // Initialize
    // =====================================================

    create() {

        this.engine = this.scene.add.image(
            -200,
            560,
            "train_engine"
        );

        this.engine.setOrigin(0.5, 1);

        this.engine.setDepth(10);

        for (let i = 0; i < this.wagonCount; i++) {

            const wagon = this.scene.add.image(

                this.engine.x - ((i + 1) * this.wagonSpacing),

                this.engine.y,

                "wagon_empty"

            );

            wagon.setOrigin(0.5, 1);

            wagon.setDepth(9);

            this.wagons.push(wagon);

        }

    }

    // =====================================================
    // Update
    // =====================================================

    update(delta) {

        // Chưa có animation ở PR này

    }

    }
