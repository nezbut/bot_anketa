{{- define "env.template" }}
- name: {{ .name }}
  valueFrom:
    secretKeyRef:
      name: "{{ .secretName }}-secret"
      key: {{ .secretKey }}
{{- end }}