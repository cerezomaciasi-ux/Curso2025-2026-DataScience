#!/usr/bin/env python3
"""
Script to transform CSV data to RDF using morph-kgc.
Uses the virtual environment at ~/Documentos/Entornos_Virtuales/DataScience
"""

import morph_kgc
import os

print("=" * 60)
print("RDF Transformation using morph-kgc")
print("=" * 60)

# Configuration for morph-kgc
config = """
[CONFIGURATION]
output_format=N-TRIPLES

[DataSource1]
mappings=mappings/hospitales.rml
"""

# Write config to file
config_path = "config.ini"
with open(config_path, "w") as f:
    f.write(config)

print(f"\n📋 Configuration file created: {config_path}")
print(f"📂 Using mapping file: mappings/hospitales.rml")
print(f"📊 Input CSV: csv/hospitales-updated.csv")

# Execute transformation
print("\n🔄 Starting RDF transformation with morph-kgc...")
try:
    # Use materialize_set to get raw N-Triples string
    triples_set = morph_kgc.materialize_set(config_path)
    
    # Convert set to N-Triples format
    output_file = "rdf/hospitales.nt"
    with open(output_file, 'w', encoding='utf-8') as f:
        for triple in sorted(triples_set):  # Sort for consistent output
            f.write(triple + '\n')
    
    print(f"\n✅ Transformation completed successfully!")
    print(f"✅ Output file: {output_file}")
    print(f"✅ Total triples generated: {len(triples_set)}")
    
    # Show some statistics
    file_size = os.path.getsize(output_file)
    print(f"\n📊 Statistics:")
    print(f"   - Triples: {len(triples_set)}")
    print(f"   - File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
    
    # Clean up config file
    os.remove(config_path)
    print(f"\n🧹 Cleaned up temporary config file")
    
except Exception as e:
    print(f"\n❌ Error during transformation: {e}")
    import traceback
    traceback.print_exc()
    if os.path.exists(config_path):
        os.remove(config_path)
    raise

print("\n" + "=" * 60)
print("Transformation complete!")
print("=" * 60)
