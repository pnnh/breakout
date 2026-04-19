components {
  id: "game"
  component: "/main/game.script"
}
components {
  id: "game_gui"
  component: "/main/game.gui"
}
embedded_components {
  id: "brick_factory"
  type: "factory"
  data: "prototype: \"/main/brick.go\"\n"
        "load_dynamically: false\n"
}
