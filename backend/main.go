package main

import "github.com/gofiber/fiber/v2"

type Reclamo struct {
	Nombre string `json:"nombre"`
	Email  string `json:"email"`
	Tipo   string `json:"tipo"`
}

func main() {
	app := fiber.New()

	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendString("API funcionando")
	})

	app.Post("/api/v1/reclamo", func(c *fiber.Ctx) error {
		var reclamo Reclamo

		if err := c.BodyParser(&reclamo); err != nil {
			return c.Status(400).SendString("Error en los datos")
		}

		return c.JSON(reclamo)
	})

	app.Listen(":3000")
}