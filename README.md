# How to use

## Setup

These steps need to be done just once.

1. Create new project with custom labeling template provided as `template.html`.

## Workflow

These steps are for the typical workflow.

1. Create data for label studio 

```
./import.py -s example/label_source.txt -t example/label_target.txt -o data.json
```

2. Import and edit the data in label studio and then export the data from label studio.

3. Convert label studio export into less verbose form

```
./export.py -i example/label_studio_export.json -o export.tsv
```

