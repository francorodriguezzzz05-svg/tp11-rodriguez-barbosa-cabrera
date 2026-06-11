package utils

import (
	"fmt"
	"os"

	"github.com/jung-kurt/gofpdf"
)

type ReclamoPDF struct {
	ID          string
	Nombre      string
	Email       string
	Tipo        string
	Direccion   string
	Descripcion string
	Estado      string
	Fecha       string
}

func GenerarPDF(reclamo ReclamoPDF) error {

	os.MkdirAll("../data/pdf", os.ModePerm)

	pdf := gofpdf.New("P", "mm", "A4", "")
	pdf.AddPage()

	pdf.SetFont("Arial", "B", 16)
	pdf.Cell(190, 10, "Comprobante de Reclamo Ciudadano")
	pdf.Ln(15)

	pdf.SetFont("Arial", "", 12)

	pdf.Cell(190, 8, "ID: "+reclamo.ID)
	pdf.Ln(8)

	pdf.Cell(190, 8, "Nombre: "+reclamo.Nombre)
	pdf.Ln(8)

	pdf.Cell(190, 8, "Email: "+reclamo.Email)
	pdf.Ln(8)

	pdf.Cell(190, 8, "Tipo: "+reclamo.Tipo)
	pdf.Ln(8)

	pdf.Cell(190, 8, "Direccion: "+reclamo.Direccion)
	pdf.Ln(8)

	pdf.Cell(190, 8, "Estado: "+reclamo.Estado)
	pdf.Ln(8)

	pdf.Cell(190, 8, "Fecha: "+reclamo.Fecha)
	pdf.Ln(12)

	pdf.MultiCell(190, 8,
		"Descripcion: "+reclamo.Descripcion,
		"", "", false)

	archivo := fmt.Sprintf("../data/pdf/reclamo_%s.pdf", reclamo.ID)

	return pdf.OutputFileAndClose(archivo)
}
