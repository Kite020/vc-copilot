import {
  Container,
  Row,
  Col,
  Card,
  Badge,
  Button,
  ListGroup,
  ProgressBar,
} from "react-bootstrap";

import { useLocation } from "react-router-dom";

function ResultPage() {
  const { state } = useLocation();
  console.log(JSON.stringify(state, null, 2));
  const riskVariant =
    state.overall_risk <= 3
      ? "success"
      : state.overall_risk <= 6
      ? "warning"
      : "danger";

  return (
    <Container className="py-5">

      {/* Header */}

      <Card
        className="shadow border-0 mb-4"
        style={{
          background:
            "linear-gradient(135deg, #0f172a, #1e293b)",
          color: "white",
          borderRadius: "20px",
        }}
      >
        <Card.Body
          className="
            d-flex
            flex-column
            align-items-center
            py-5
          "
        >
          <h1
            style={{
              fontWeight: "700",
              fontSize: "4rem",
            }}
          >
            {state.startup_name}
          </h1>

          <Badge
            bg={
              state.recommendation === "INVEST"
                ? "success"
                : "danger"
            }
            style={{
              fontSize: "1.1rem",
              padding: "12px 28px",
            }}
          >
            {state.recommendation}
          </Badge>
        </Card.Body>
      </Card>

      <Card
        className="shadow-sm mb-4"
        style={{
          borderRadius: "16px",
        }}
      >
        <Card.Body className="py-4">
          <h3 className="mb-3">
            Startup Overview
          </h3>

          <p
            className="mb-0"
            style={{
              fontSize: "1.05rem",
            }}
          >
            {state.startup_summary ||
              "AI-powered startup analysis generated from the uploaded pitch deck."}
          </p>
        </Card.Body>
      </Card>

      {/* Metrics */}

      <Row className="g-4 mb-4">

        {/* Investment Score */}

        <Col md={4}>
          <Card
            className="shadow-sm h-100"
            style={{
              borderRadius: "16px",
              minHeight: "260px",
            }}
          >
            <Card.Body
              className="
                d-flex
                flex-column
                justify-content-center
                text-center
              "
            >
              <h4>Investment Score</h4>

              <h1
                style={{
                  fontSize: "4rem",
                  color: "#16a34a",
                  fontWeight: "700",
                }}
              >
                {state.investment_score}
              </h1>

              <ProgressBar
                now={state.investment_score}
                label={`${state.investment_score}%`}
              />
            </Card.Body>
          </Card>
        </Col>

        {/* Risk */}

        <Col md={4}>
          <Card
            className="shadow-sm h-100"
            style={{
              borderRadius: "16px",
              minHeight: "260px",
            }}
          >
            <Card.Body
              className="
                d-flex
                flex-column
                justify-content-center
                text-center
              "
            >
              <h4>Overall Risk</h4>

              <h1
                style={{
                  fontSize: "4rem",
                  fontWeight: "700",
                }}
              >
                {state.overall_risk}
              </h1>

              <Badge
                bg={riskVariant}
                style={{
                  fontSize: "1rem",
                  padding: "10px",
                }}
              >
                {state.overall_risk <= 3
                  ? "Low Risk"
                  : state.overall_risk <= 6
                  ? "Medium Risk"
                  : "High Risk"}
              </Badge>
            </Card.Body>
          </Card>
        </Col>

        {/* Founder */}

        <Col md={4}>
          <Card
            className="shadow-sm h-100"
            style={{
              borderRadius: "16px",
              minHeight: "260px",
            }}
          >
            <Card.Body
              className="
                d-flex
                flex-column
                justify-content-center
                text-center
              "
            >
              <h4>Founder Score</h4>

              <h1
                style={{
                  fontSize: "4rem",
                  fontWeight: "700",
                }}
              >
                {state.founder_score}
              </h1>

              <p
                style={{
                  color: "#16a34a",
                  fontWeight: "600",
                }}
              >
                Excellent
              </p>
            </Card.Body>
          </Card>
        </Col>

      </Row>

      {/* Investment Result */}

      <Card
        className="shadow border-0 mb-4"
        style={{
          borderRadius: "16px",
        }}
      >
        <Card.Body>

          <h3>
            Investment Decision
          </h3>

          <hr />

          <h1
            style={{
              color:
                state.recommendation === "INVEST"
                  ? "#16a34a"
                  : "#dc2626",
              fontWeight: "700",
            }}
          >
            {state.recommendation}
          </h1>

          <p
            style={{
              fontSize: "1.1rem",
            }}
          >
            Investment Score:
            {" "}
            <strong>
              {state.investment_score}/100
            </strong>
          </p>

          <p>
            Based on market opportunity,
            founder quality, competition,
            execution feasibility and
            overall risk assessment.
          </p>

        </Card.Body>
      </Card>

      {/* Competitors */}

      <Card
        className="shadow-sm mb-4"
        style={{
          borderRadius: "16px",
        }}
      >
        <Card.Body>
          <h3 className="mb-4">
            Top Competitors
          </h3>

          <Row>

            {(state.competitors || []).map(
              (item) => (
                <Col md={6} key={item}>
                  <p
                    style={{
                      fontSize: "1.1rem",
                    }}
                  >
                    ✅ {item}
                  </p>
                </Col>
              )
            )}

          </Row>
        </Card.Body>
      </Card>

      
      <Row className="g-4 mb-4">

        <Col md={6}>
          <Card className="shadow-sm h-100">
            <Card.Body>

              <h4>
                Founder Strengths
              </h4>

              <ListGroup variant="flush">

                {(state.founder_strengths || []).map(
                  (item) => (
                    <ListGroup.Item key={item}>
                      ✅ {item}
                    </ListGroup.Item>
                  )
                )}

              </ListGroup>

            </Card.Body>
          </Card>
        </Col>

        <Col md={6}>
          <Card className="shadow-sm h-100">
            <Card.Body>

              <h4>
                Founder Risks
              </h4>

              <ListGroup variant="flush">

                {(state.founder_risks || []).map(
                  (item) => (
                    <ListGroup.Item key={item}>
                      ⚠️ {item}
                    </ListGroup.Item>
                  )
                )}

              </ListGroup>

            </Card.Body>
          </Card>
        </Col>

      </Row>
      <Row className="g-4 mb-4">

        <Col md={6}>
          <Card className="shadow-sm h-100">
            <Card.Body>

              <h4>
                Reasons To Invest
              </h4>

              <ListGroup variant="flush">

                {(state.reasons || []).map(
                  (item) => (
                    <ListGroup.Item key={item}>
                      🚀 {item}
                    </ListGroup.Item>
                  )
                )}

              </ListGroup>

            </Card.Body>
          </Card>
        </Col>

        <Col md={6}>
          <Card className="shadow-sm h-100">
            <Card.Body>

              <h4>
                Due Diligence Next Steps
              </h4>

              <ListGroup variant="flush">

                {(state.next_steps || []).map(
                  (item) => (
                    <ListGroup.Item key={item}>
                      📌 {item}
                    </ListGroup.Item>
                  )
                )}

              </ListGroup>

            </Card.Body>
          </Card>
        </Col>

      </Row>

      <Card className="shadow-sm mb-4">
        <Card.Body>

          <h4>
            Risk Breakdown
          </h4>

          <br />

          <p>Market Risk</p>

          <ProgressBar
            now={state.market_risk * 10}
            label={state.market_risk}
            className="mb-3"
          />

          <p>Competition Risk</p>

          <ProgressBar
            now={state.competition_risk * 10}
            label={state.competition_risk}
            className="mb-3"
          />

          <p>Execution Risk</p>

          <ProgressBar
            now={state.execution_risk * 10}
            label={state.execution_risk}
            className="mb-3"
          />

          <p>Funding Risk</p>

          <ProgressBar
            now={state.funding_risk * 10}
            label={state.funding_risk}
            className="mb-3"
          />

          <p>Founder Risk</p>

          <ProgressBar
            now={state.founder_risk * 10}
            label={state.founder_risk}
          />

        </Card.Body>
      </Card>
      
      <Card className="shadow-sm mb-4">
        <Card.Body>

          <h4>
            Risk Assessment
          </h4>

          <p>
            {state.risk_summary}
          </p>

        </Card.Body>
      </Card>

      {/* Download */}

      <div className="mb-4">

        <Button
          size="lg"
          variant="dark"
          onClick={() =>
            window.open(
              "http://127.0.0.1:8000/download-memo",
              "_blank"
            )
          }
        >
          Download Investment Memo
        </Button>

      </div>

    </Container>
  );
}

export default ResultPage;