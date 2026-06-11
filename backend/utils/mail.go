package utils

import (
	"bytes"
	"encoding/json"
	"net/http"
)

type MailRequest struct {
	Email     string `json:"email"`
	Nombre    string `json:"nombre"`
	IDReclamo string `json:"id_reclamo"`
	Tipo      string `json:"tipo"`
	Estado    string `json:"estado"`
}

func EnviarMailMock(mail MailRequest) error {

	body, err := json.Marshal(mail)
	if err != nil {
		return err
	}

	_, err = http.Post(
		"http://mail-mock:9000/send",
		"application/json",
		bytes.NewBuffer(body),
	)

	return err
}
