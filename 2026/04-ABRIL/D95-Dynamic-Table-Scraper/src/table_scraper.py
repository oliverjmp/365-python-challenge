import pandas as pd
from bs4 import BeautifulSoup
from typing import Optional

class DynamicTableScraper:
    def __init__(self, html_content: str):
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def scrape_table(self, table_id: Optional[str] = None, table_class: Optional[str] = None) -> pd.DataFrame:
        """Extrae datos de una tabla HTML convirtiendo tipos numéricos automáticamente."""
        try:
            attrs = {}
            if table_id: attrs['id'] = table_id
            if table_class: attrs['class'] = table_class
            
            table = self.soup.find('table', attrs=attrs)
            if not table:
                return pd.DataFrame()

            rows = []
            for tr in table.find_all('tr'):
                cells = [cell.get_text(strip=True) for cell in tr.find_all(['td', 'th'])]
                if cells:
                    rows.append(cells)
            
            if not rows:
                return pd.DataFrame()

            df = pd.DataFrame(rows[1:], columns=rows[0])
            
            # Usamos 'coerce' en lugar de 'ignore' para compatibilidad con Pandas
            for col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(df[col])
            
            return df
        except Exception:
            return pd.DataFrame()