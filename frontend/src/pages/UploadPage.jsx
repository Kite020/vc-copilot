import { Container, Card, Button, Form } from "react-bootstrap";
import { useState } from "react";
import API from "../services/api";
import { useNavigate } from "react-router-dom";

function UploadPage() {
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleAnalyze = async () => {
        if (!file) return;
      
        try {
          setLoading(true);
      
          const formData = new FormData();
      
          formData.append(
            "file",
            file
          );
      
          const response =
            await API.post(
              "/analyze-deck",
              formData,
              {
                headers: {
                  "Content-Type":
                    "multipart/form-data",
                },
              }
            );
            if (response.data.error) {
              alert(response.data.error);
              return;
            }
      
            navigate(
                "/results",
                {
                  state: response.data,
                }
              );
      
        } catch (error) {
          console.error(error);
        } finally {
          setLoading(false);
        }
      };

  return (
    <Container
      className="d-flex justify-content-center align-items-center"
      style={{ minHeight: "100vh" }}
    >
      <Card
        style={{
          width: "500px",
          padding: "30px",
          borderRadius: "20px",
        }}
      >
        <h2 className="text-center mb-4">
          VC Copilot
        </h2>

        <p className="text-center text-muted">
          Upload a startup pitch deck and receive
          an AI-powered investment recommendation.
        </p>

        <Form.Group className="mb-3">
          <Form.Control
            type="file"
            accept=".pdf"
            onChange={(e) =>
              setFile(e.target.files[0])
            }
          />
        </Form.Group>

        {file && (
          <p>
            Selected:
            {" "}
            {file.name}
          </p>
        )}

        <Button
        variant="primary"
        className="w-100"
        onClick={handleAnalyze}
        disabled={loading}
        >
        {loading
            ? "Analyzing..."
            : "Analyze Deck"}
        </Button>
      </Card>
    </Container>
  );
}

export default UploadPage;