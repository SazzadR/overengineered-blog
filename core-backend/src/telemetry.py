from fastapi import FastAPI

from opentelemetry import metrics
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource


def setup_telemetry(app: FastAPI):
    resource = Resource.create({"service.name": "core-backend"})
    exporter = OTLPMetricExporter(endpoint="http://otel-collector:4318/v1/metrics")
    reader = PeriodicExportingMetricReader(exporter, export_interval_millis=5000)
    provider = MeterProvider(resource=resource, metric_readers=[reader])
    metrics.set_meter_provider(provider)

    FastAPIInstrumentor.instrument_app(app)
