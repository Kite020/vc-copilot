import { Container, Card, Badge } from "react-bootstrap";
import { useLocation } from "react-router-dom";

function ResultPage() {

  const { state } = useLocation();

  return (
    <Container
      className="py-5"
    >
      <Card
        className="p-4"
      >

        <h2>
          {state.startup_name}
        </h2>

        <hr />

        <h4>
          Recommendation:
          {" "}
          <Badge bg="success">
            {state.recommendation}
          </Badge>
        </h4>

        <h4 className="mt-3">
          Investment Score:
          {" "}
          {state.investment_score}/100
        </h4>

        <h4 className="mt-3">
          Overall Risk:
          {" "}
          {state.overall_risk}/10
        </h4>

        <h4 className="mt-4">
          Founder Score:
          {" "}
          {state.founder_score}/10
        </h4>

        <h4 className="mt-4">
          Competitors
        </h4>

        <ul>
          {state.competitors.map(
            (competitor) => (
              <li key={competitor}>
                {competitor}
              </li>
            )
          )}
        </ul>

      </Card>
    </Container>
  );
}

export default ResultPage;