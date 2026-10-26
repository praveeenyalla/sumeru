import random
import datetime
from typing import Dict, Optional
from app.models.domain import NodeTelemetry, ClusterTelemetryResponse

class TelemetryService:
    BASE_NODES = {
        "SUMERU_CORE": {
            "name": "CENTRAL SYNAPSE ORCHESTRATOR",
            "category": "COORDINATOR",
            "base_latency": 0.4,
            "status": "MASTER CLUSTER OPTIMAL",
            "protocol": "TLS 1.3 / SOV-IPC",
            "base_ops": 184000
        },
        "AI_CORE": {
            "name": "SOVEREIGN SLM REASONING MESH",
            "category": "INTELLIGENCE",
            "base_latency": 3.8,
            "status": "ISOLATED TENANT HEALTHY",
            "protocol": "gRPC v2 / mTLS",
            "base_ops": 64200
        },
        "SAP_CORE": {
            "name": "SAP S/4HANA CLEAN CORE KERNEL",
            "category": "ERP_ENGINE",
            "base_latency": 1.8,
            "status": "CLEAN CORE EXTENSIONS COMPLIANT",
            "protocol": "OData v4 / Event Mesh",
            "base_ops": 92100
        },
        "CLOUD_INFRA": {
            "name": "HYBRID MULTI-CLOUD FABRIC",
            "category": "INFRASTRUCTURE",
            "base_latency": 2.1,
            "status": "MULTI-REGION REPLICATED",
            "protocol": "WireGuard / BGP",
            "base_ops": 145000
        },
        "DATA_FABRIC": {
            "name": "MASTER DATA LAKEHOUSE (MDM)",
            "category": "DATA_MANAGEMENT",
            "base_latency": 4.2,
            "status": "PARQUET STREAM HARMONIZED",
            "protocol": "Apache Kafka / Iceberg",
            "base_ops": 118000
        },
        "SECURITY": {
            "name": "ZERO-TRUST CRYPTOGRAPHIC DEFENSE",
            "category": "DEFENSIVE_SECURITY",
            "base_latency": 0.9,
            "status": "ZERO BREACH ANOMALIES",
            "protocol": "KMS HSM / FIPS 140-3",
            "base_ops": 210000
        },
        "ENGINEERING": {
            "name": "POLYGLOT CORE ENGINE NODES",
            "category": "RUNTIME_ENGINE",
            "base_latency": 1.1,
            "status": "LOW-LATENCY GO/RUST POOL",
            "protocol": "QUIC / REST-v3",
            "base_ops": 178000
        }
    }

    def get_cluster_telemetry(self) -> ClusterTelemetryResponse:
        nodes: Dict[str, NodeTelemetry] = {}
        total_lat = 0.0
        now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

        for node_id, meta in self.BASE_NODES.items():
            # Add dynamic jitter to simulate real-world enterprise telemetry
            jitter = random.uniform(-0.15, 0.15)
            lat = max(0.2, round(meta["base_latency"] + jitter, 2))
            total_lat += lat
            ops = int(meta["base_ops"] + random.randint(-2500, 2500))
            cpu = round(random.uniform(18.5, 42.0), 1)
            mem = round(random.uniform(32.0, 58.5), 1)

            nodes[node_id] = NodeTelemetry(
                node_id=node_id,
                name=meta["name"],
                category=meta["category"],
                latency_ms=lat,
                status=meta["status"],
                protocol=meta["protocol"],
                throughput_ops=ops,
                memory_usage_pct=mem,
                cpu_usage_pct=cpu,
                last_heartbeat=now_utc
            )

        avg_lat = round(total_lat / len(self.BASE_NODES), 2)
        return ClusterTelemetryResponse(
            cluster_state="SYNAPSE_HARMONIZED_NOMINAL",
            active_nodes=len(self.BASE_NODES),
            total_nodes=len(self.BASE_NODES),
            global_average_latency_ms=avg_lat,
            synapse_version="4.8.2-PROD",
            utc_timestamp=now_utc,
            nodes=nodes
        )

    def get_single_node(self, node_id: str) -> Optional[NodeTelemetry]:
        telemetry = self.get_cluster_telemetry()
        return telemetry.nodes.get(node_id)

telemetry_service = TelemetryService()
