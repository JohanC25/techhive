import { createVNode, render } from 'vue'
import html2pdf from 'html2pdf.js'
import OrdenRecepcionA4 from '@/components/OrdenRecepcionA4.vue'
import OrdenRecepcionTicket from '@/components/OrdenRecepcionTicket.vue'

export function useDescargarPDF(recepcion: any, cliente: any) {
  const descargar = async (formato: 'a4' | 'ticket') => {
    const container = document.createElement('div')
    document.body.appendChild(container)

    const component = formato === 'a4'
      ? createVNode(OrdenRecepcionA4, { recepcion, cliente })
      : createVNode(OrdenRecepcionTicket, { recepcion, cliente })

    render(component, container)

    await new Promise(resolve => setTimeout(resolve, 200)) // espera para renderizar

    const element = container.querySelector('div')
    if (!element) return

    await html2pdf()
      .set({
        margin: 10,
        filename: `OrdenRecepcion-${recepcion.id}.pdf`,
        html2canvas: { scale: 2 },
        jsPDF: { 
          unit: 'mm', 
          format: formato === 'a4' ? 'a4' : [80, 200], 
          orientation: 'portrait' 
        }
      })
      .from(element)
      .save()

    render(null, container)
    document.body.removeChild(container)
  }

  return { descargar }
}
