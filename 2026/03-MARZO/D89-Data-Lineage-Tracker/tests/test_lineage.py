import pytest
from src.lineage_tracker import DataLineageTracker

def test_register_and_get_lineage():
    """Valida que las transformaciones se registren y recuperen correctamente."""
    tracker = DataLineageTracker()
    
    tracker.register_transformation("raw_sales", "cleaned_sales", "filter_nulls")
    tracker.register_transformation("cleaned_sales", "aggregated_sales", "group_by_region")
    
    lineage = tracker.get_lineage("aggregated_sales")
    
    assert len(lineage) == 1
    assert lineage[0]["source"] == "cleaned_sales"
    assert lineage[0]["operation"] == "group_by_region"

def test_get_empty_lineage():
    """Valida que se devuelva una lista vacía si el dataset no tiene registros previos."""
    tracker = DataLineageTracker()
    lineage = tracker.get_lineage("unknown_dataset")
    assert lineage == []