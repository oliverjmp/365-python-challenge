import os
from src.doc_engine import get_project_docs_status, generate_doc_summary

def test_get_project_docs_status():
    files = get_project_docs_status("docs")
    assert isinstance(files, list)
    assert "index.md" in files

def test_get_project_docs_status_not_found():
    files = get_project_docs_status("non_existent_folder_xyz")
    assert files == []

def test_generate_doc_summary():
    summary = generate_doc_summary("D179-Automated-Documentation")
    assert "D179-Automated-Documentation" in summary
    assert "=== Documentación Oficial" in summary