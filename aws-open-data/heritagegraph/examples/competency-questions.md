# Competency Questions → TBox-Only SPARQL ASK Queries

These ASK queries validate that the ontology schema contains the required classes and properties to answer each CQ. They do **not** require instance data.

**Prefixes used in all queries**
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX prov: <http://www.w3.org/ns/prov#>
```

**Structural Questions**

CQ1. Which architectural structures were built during [time period] using [architectural style]?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
ASK WHERE {
  heritageGraph:ArchitecturalStructure a owl:Class .
  heritageGraph:Production a owl:Class .
  heritageGraph:TimeSpan a owl:Class .
  heritageGraph:has_architectural_style a owl:ObjectProperty .
  heritageGraph:has_architectural_style rdfs:range heritageGraph:ArchitecturalStyleEnum .
  heritageGraph:was_produced_by_event a owl:ObjectProperty .
  heritageGraph:has_timespan a owl:ObjectProperty .
  heritageGraph:date_earliest a owl:DatatypeProperty .
  heritageGraph:date_latest a owl:DatatypeProperty .
}
```

CQ2. Which architectural elements (e.g., Pinnacle) are components of structures used in a given ritual?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:ArchitecturalElement a owl:Class .
  heritageGraph:ArchitecturalStructure a owl:Class .
  heritageGraph:RitualEvent a owl:Class .
  heritageGraph:is_component_of a owl:ObjectProperty .
  heritageGraph:participates_in_ritual a owl:ObjectProperty .
}
```

CQ3. Which iconographic objects depict [deity], and where are they currently located?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:IconographicObject a owl:Class .
  heritageGraph:Deity a owl:Class .
  heritageGraph:Place a owl:Class .
  heritageGraph:depicts_deity a owl:ObjectProperty .
  heritageGraph:has_current_location a owl:ObjectProperty .
}
```

CQ4. Which heritage structures are associated with historical events such as earthquakes, restoration activities, or political transitions, and what are the types and time-spans of those events?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:ArchitecturalStructure a owl:Class .
  heritageGraph:HistoricalEvent a owl:Class .
  heritageGraph:TimeSpan a owl:Class .
  heritageGraph:architectural_structures a owl:ObjectProperty .
  heritageGraph:has_timespan a owl:ObjectProperty .
}
```

CQ5. Which architectural structures within a given geographical area belong to a particular architectural typology (temple, palace, monastery, shrine, etc.)?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
ASK WHERE {
  heritageGraph:Place a owl:Class .
  heritageGraph:ArchitecturalStructure a owl:Class .
  heritageGraph:contains_structure a owl:ObjectProperty .
  FILTER EXISTS { ?t rdfs:subClassOf heritageGraph:ArchitecturalStructure }
}
```

CQ6. Which heritage shares a common architectural style?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
ASK WHERE {
  heritageGraph:ArchitecturalStructure a owl:Class .
  heritageGraph:has_architectural_style a owl:ObjectProperty .
  heritageGraph:has_architectural_style rdfs:range heritageGraph:ArchitecturalStyleEnum .
}
```

**Rituals, Festivals, and Temporal Structure**

CQ7. Which religious or sacred structures in [place] are associated with which deities or spiritual figures?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:Temple a owl:Class .
  heritageGraph:Enshrinement a owl:Class .
  heritageGraph:Deity a owl:Class .
  heritageGraph:enshrines_deity_through_event a owl:ObjectProperty .
  heritageGraph:enshrined_deity a owl:ObjectProperty .
  heritageGraph:enshrined_in_structure a owl:ObjectProperty .
  heritageGraph:took_place_at a owl:ObjectProperty .
}
```

CQ8. Among the active temples that conduct daily Nitya Puja, which ones are currently assessed as being in “Poor” or “Endangered” condition?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:Temple a owl:Class .
  heritageGraph:RitualEvent a owl:Class .
  heritageGraph:ConditionAssessment a owl:Class .
  heritageGraph:ConditionState a owl:Class .
  heritageGraph:has_condition_assessment a owl:ObjectProperty .
  heritageGraph:assessed_condition_state a owl:ObjectProperty .
  heritageGraph:has_condition_type a owl:ObjectProperty .
  heritageGraph:ritual_type a owl:ObjectProperty .
}
```

CQ9. Which social/caste groups have hereditary roles in specific rituals that are critical for the festival's completion?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:CasteGroup a owl:Class .
  heritageGraph:RitualEvent a owl:Class .
  heritageGraph:performed_by_group a owl:ObjectProperty .
  heritageGraph:is_critical_for_festival a owl:DatatypeProperty .
  heritageGraph:traditional_role a owl:DatatypeProperty .
}
```

CQ10. Which ritual objects (iconographic objects, ritual chariots) are associated with rituals, and which individuals or groups are responsible for their use?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:IconographicObject a owl:Class .
  heritageGraph:RitualEvent a owl:Class .
  heritageGraph:participates_in_ritual a owl:ObjectProperty .
  heritageGraph:used_by a owl:ObjectProperty .
}
```

CQ11. Which rituals or festivals are associated with specific heritage sites or places, which sacred figures they invoke, and what are their recurrence patterns?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:RitualEvent a owl:Class .
  heritageGraph:Festival a owl:Class .
  heritageGraph:ritual_on_structure a owl:ObjectProperty .
  heritageGraph:took_place_at a owl:ObjectProperty .
  heritageGraph:invokes_deity a owl:ObjectProperty .
  heritageGraph:recurrence_pattern a owl:DatatypeProperty .
}
```

CQ12. What is the canonical sequence of ritual events within a festival cycle, and which actors are responsible for each step?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:RitualEvent a owl:Class .
  heritageGraph:Festival a owl:Class .
  heritageGraph:occurs_before a owl:ObjectProperty .
  heritageGraph:occurs_after a owl:ObjectProperty .
  heritageGraph:carried_out_by a owl:ObjectProperty .
  heritageGraph:performed_by_group a owl:ObjectProperty .
}
```

CQ13. Which rituals involve moving sacred presences or icons between sites, and what routes and places are traversed?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:RitualEvent a owl:Class .
  heritageGraph:route_places a owl:ObjectProperty .
  heritageGraph:start_place a owl:ObjectProperty .
  heritageGraph:end_place a owl:ObjectProperty .
  heritageGraph:route_description a owl:DatatypeProperty .
}
```

CQ14. How do major crises trigger extraordinary or temporary rituals, and how do these relate to the normal ritual calendar?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:HistoricalEvent a owl:Class .
  heritageGraph:RitualEvent a owl:Class .
  heritageGraph:includes_ritual_event a owl:ObjectProperty .
  heritageGraph:recurrence_pattern a owl:DatatypeProperty .
}
```

CQ15. What materials, techniques, and sensory elements are used in key ritual events, and how do these vary across traditions and sites?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:RitualEvent a owl:Class .
  heritageGraph:Material a owl:Class .
  heritageGraph:Technique a owl:Class .
  heritageGraph:used_materials a owl:ObjectProperty .
  heritageGraph:used_technique a owl:ObjectProperty .
  heritageGraph:has_religious_tradition a owl:ObjectProperty .
  heritageGraph:took_place_at a owl:ObjectProperty .
}
```

CQ16. How do ritual obligations differ for participant groups, and how are roles recorded or enforced?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:RitualEvent a owl:Class .
  heritageGraph:performed_by_group a owl:ObjectProperty .
  heritageGraph:traditional_role a owl:DatatypeProperty .
}
```

CQ17. Which rituals or festivals have documented transformations, and which events, policies, or actors drove those changes?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:RitualEvent a owl:Class .
  heritageGraph:Festival a owl:Class .
  heritageGraph:HeritageAssertion a owl:Class .
  heritageGraph:DataSource a owl:Class .
  heritageGraph:was_derived_from_source a owl:ObjectProperty .
  heritageGraph:was_attributed_to_agent a owl:ObjectProperty .
}
```

CQ18. How do changes in object location, ritual practice, and structure modification reflect broader historical or political transitions?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:ArchitecturalStructure a owl:Class .
  heritageGraph:RitualEvent a owl:Class .
  heritageGraph:HistoricalEvent a owl:Class .
  heritageGraph:has_current_location a owl:ObjectProperty .
  heritageGraph:participates_in_ritual a owl:ObjectProperty .
  heritageGraph:has_provenance_assertion a owl:ObjectProperty .
}
```

**Institutions and Syncretism**

CQ19. Which organizations manage which heritage, perform which rituals, and hold custody of heritage assets?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:Guthi a owl:Class .
  heritageGraph:managed_by_guthi a owl:ObjectProperty .
  heritageGraph:performs_ritual a owl:ObjectProperty .
  heritageGraph:holds_custody_of a owl:ObjectProperty .
}
```

CQ20. Which structures or objects were commissioned by a specific patron, ruler, monastic order, or community group?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:Production a owl:Class .
  heritageGraph:commissioned_by a owl:ObjectProperty .
  heritageGraph:produced_object a owl:ObjectProperty .
}
```

CQ21. Which institutions or endowments provide economic and ritual support for specific sites, rituals, or living sacred figures?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:Guthi a owl:Class .
  heritageGraph:supported_by_institution a owl:ObjectProperty .
  heritageGraph:Temple a owl:Class .
  heritageGraph:RitualEvent a owl:Class .
  heritageGraph:LivingGoddessTenure a owl:Class .
}
```

CQ22. Which festivals bring together practitioners from multiple traditions around a shared syncretic deity, and what roles do different groups play?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:Festival a owl:Class .
  heritageGraph:SyncreticRelationship a owl:Class .
  heritageGraph:assigned_to_deity a owl:ObjectProperty .
  heritageGraph:assigned_equivalent a owl:ObjectProperty .
  heritageGraph:performed_by_group a owl:ObjectProperty .
  heritageGraph:has_religious_tradition a owl:ObjectProperty .
}
```

CQ23. Which places or structures function as shared or contested sites for multiple traditions?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:Place a owl:Class .
  heritageGraph:ArchitecturalStructure a owl:Class .
  heritageGraph:has_religious_tradition a owl:ObjectProperty .
}
```

CQ24. Which rituals at Hindu temples and Buddhist monuments invoke the same syncretic deity, and how do their ritual roles differ?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:RitualEvent a owl:Class .
  heritageGraph:Temple a owl:Class .
  heritageGraph:BuddhistMonument a owl:Class .
  heritageGraph:invokes_deity a owl:ObjectProperty .
  heritageGraph:performed_by_group a owl:ObjectProperty .
}
```

CQ25. How do syncretic sacred figures or deities link Hindu, Buddhist, and local practices across places and periods, and what evidence supports these links?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:SyncreticRelationship a owl:Class .
  heritageGraph:assigned_to_deity a owl:ObjectProperty .
  heritageGraph:assigned_equivalent a owl:ObjectProperty .
  heritageGraph:was_derived_from_source a owl:ObjectProperty .
  heritageGraph:documented_in_source a owl:ObjectProperty .
  heritageGraph:Place a owl:Class .
  heritageGraph:TimeSpan a owl:Class .
}
```

**Living Goddess (Kumari)**

CQ26. Which girl was serving as Living Goddess (Kumari) for which period, at which Kumari Ghar?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:LivingGoddessTenure a owl:Class .
  heritageGraph:Person a owl:Class .
  heritageGraph:ArchitecturalStructure a owl:Class .
  heritageGraph:had_participant a owl:ObjectProperty .
  heritageGraph:residence_structure a owl:ObjectProperty .
  heritageGraph:has_timespan a owl:ObjectProperty .
}
```

CQ27. For a given Kumari-person, which deity is believed to be present, and in which religious traditions?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:LivingGoddessTenure a owl:Class .
  heritageGraph:Deity a owl:Class .
  heritageGraph:embodied_deity a owl:ObjectProperty .
  heritageGraph:has_religious_tradition a owl:ObjectProperty .
}
```

CQ28. How does the Kumari institution embody Hindu–Buddhist syncretism in a specific place and period?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:LivingGoddessTenure a owl:Class .
  heritageGraph:SyncreticRelationship a owl:Class .
  heritageGraph:Place a owl:Class .
  heritageGraph:TimeSpan a owl:Class .
  heritageGraph:assigned_to_deity a owl:ObjectProperty .
  heritageGraph:assigned_equivalent a owl:ObjectProperty .
}
```

CQ29. What daily rituals does a specific Kumari perform at Kumari Ghar, and what is their temporal pattern?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:RitualEvent a owl:Class .
  heritageGraph:LivingGoddessTenure a owl:Class .
  heritageGraph:ritual_type a owl:ObjectProperty .
  heritageGraph:ritual_on_structure a owl:ObjectProperty .
  heritageGraph:recurrence_pattern a owl:DatatypeProperty .
}
```

CQ30. In which festivals and processions does a given Kumari participate, and what is the ritual sequence?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:Festival a owl:Class .
  heritageGraph:RitualEvent a owl:Class .
  heritageGraph:occurs_before a owl:ObjectProperty .
  heritageGraph:occurs_after a owl:ObjectProperty .
  heritageGraph:had_participant a owl:ObjectProperty .
}
```

CQ31. Which institution bears economic/ritual responsibility for a given Kumari during her tenure?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:LivingGoddessTenure a owl:Class .
  heritageGraph:supported_by_institution a owl:ObjectProperty .
  heritageGraph:Guthi a owl:Class .
}
```

CQ32. When and why did an individual stop being Kumari, and what event terminated her divine status?
```sparql
PREFIX heritageGraph: <https://cair-nepal.org/heritagegraph/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
ASK WHERE {
  heritageGraph:LivingGoddessRetirement a owl:Class .
  heritageGraph:ended_tenure_of a owl:ObjectProperty .
  heritageGraph:has_timespan a owl:ObjectProperty .
  heritageGraph:note a owl:DatatypeProperty .
}
```
