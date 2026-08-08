/*
=====================================================
 TrainBuilder
 Main Entry Point
=====================================================
*/

import { Game } from "./core/game.js";

window.addEventListener("load", () => {

    const game = new Game();

    game.start();

});
