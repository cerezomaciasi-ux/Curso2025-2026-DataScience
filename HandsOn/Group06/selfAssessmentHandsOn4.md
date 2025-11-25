# Self-Assessment for Hands-On Assignment 4

## Group Information
- **Group:** Group06
- **Assignment:** Hands-On 4 - RML Mappings and RDF Transformation
- **Date:** 2025-11-25

## Deliverables Checklist

- [x] **RML Mapping File** (`mappings/hospitales.rml`)
  - Created RML mappings for hospital data
  - Mapped all CSV columns to ontology properties
  - Included proper data type specifications (xsd:string, xsd:integer, xsd:dateTime)
  
- [x] **YARRRML Mapping File** (`mappings/hospitales.yml`)
  - Created YARRRML version for better readability
  - Provides same mappings in simplified YAML syntax
  
- [x] **RDF Output File** (`rdf/hospitales.nt`)
  - Generated 744 RDF triples from 62 hospital records
  - Output in NTriples format as required
  - All data properties correctly mapped

- [x] **Self-Assessment Document** (`selfAssessmentHandsOn4.md`)
  - This document

## Mapping Strategy

### Data Source
- **CSV File:** `csv/hospitales-updated.csv`
- **Records:** 62 hospitals in Valencia
- **Columns:** 14 columns including name, type, financing, beds, location, dates, and geographic data

### Ontology Alignment
The mappings align with the existing `ontology/ontology.ttl` which defines:
- **Main Class:** `ns:Hospital`
- **Data Properties:** 11 properties covering all hospital attributes
- **Data Types:** Properly typed as strings, integers, and dateTime values

### Transformation Process
1. Created RML and YARRRML mapping files based on provided templates
2. Mapped each CSV column to corresponding ontology property:
   - `Nombre` → `ns:isNamed` (string)
   - `Financiaci` → `ns:isFinancedby` (string)
   - `Tipo` → `ns:isType` (string)
   - `Camas` → `ns:hasBeds` (integer)
   - `Direccion` → `ns:isLocatedin` (string)
   - `Fecha` → `ns:wasCreatedin` (dateTime)
   - `Barrio` → `ns:estaEnbarrio` (string)
   - `codbarrio` → `ns:tieneCodigodeBarrio` (integer)
   - `coddistbar` → `ns:tieneCoddistBarrio` (integer)
   - `coddistrit` → `ns:tieneCodigodistrito` (integer)
   - `Geo Shape` → `ns:hasShape` (string)

3. Used hospital name as URI identifier with proper URL encoding
4. Executed transformation using **morph-kgc** library from virtual environment (`~/Documentos/Entornos_Virtuales/DataScience`)
5. Generated NTriples output with 744 triples (128 KB)

## Challenges and Solutions

### Challenge 1: morph-kgc Installation
- **Issue:** Could not install morph-kgc in system Python due to externally-managed environment
- **Solution:** Used existing virtual environment at `~/Documentos/Entornos_Virtuales/DataScience` where morph-kgc was already installed

### Challenge 2: File Path Configuration
- **Issue:** RML mappings initially used relative path `../csv/` which didn't work from execution directory
- **Solution:** Updated RML and YARRRML files to use `csv/hospitales-updated.csv` relative to project root

### Challenge 3: NTriples Serialization
- **Issue:** morph-kgc's default `materialize()` function had issues parsing generated triples with JSON strings
- **Solution:** Used `materialize_set()` function which returns raw N-Triples strings, avoiding the re-parsing step

### Challenge 4: Special Characters in URIs
- **Issue:** Hospital names contain spaces and special characters that are invalid in URIs
- **Solution:** morph-kgc automatically handles URL encoding, creating valid URIs like `Hospital%20pare%20Jofre`

## Verification

### Output Validation
- **Total Triples:** 744 (62 hospitals × 12 properties each)
- **Format:** Valid NTriples syntax
- **File Size:** 128 KB
- **Encoding:** UTF-8 with proper escaping of special characters
- **Sample Triple:**
  ```
  <http://www.owl-ontologies.com/ns#Hospital/Hospital%20pare%20Jofre> <http://www.owl-ontologies.com/ns#isNamed> "Hospital pare Jofre"
  ```

### Quality Checks
- ✓ All 62 hospitals successfully transformed
- ✓ All properties mapped correctly
- ✓ Data types properly specified
- ✓ URIs properly encoded
- ✓ NTriples syntax validated

## Learning Outcomes

1. **RML Mapping:** Understood how to create RML mappings to transform CSV data to RDF
2. **YARRRML:** Learned the simplified YARRRML syntax as an alternative to RML
3. **Data Type Handling:** Gained experience with XSD data types in RDF
4. **URI Design:** Learned best practices for creating valid URIs from text data
5. **RDF Serialization:** Understood NTriples format and its syntax requirements

## Conclusion

All deliverables have been successfully completed. The hospital data has been transformed into RDF format using **morph-kgc** library, following the existing ontology structure with proper mappings and data type specifications. The transformation generated 744 valid RDF triples representing 62 hospitals with all their attributes.

**Tools Used:**
- morph-kgc (from virtual environment `~/Documentos/Entornos_Virtuales/DataScience`)
- Python 3.12
- RML and YARRRML mapping languages
