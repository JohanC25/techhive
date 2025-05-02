import { createVNode, render } from 'vue'
import OrdenRecepcionA4 from '@/components/OrdenRecepcionA4.vue'
import OrdenRecepcionTicket from '@/components/OrdenRecepcionTicket.vue'

export function useImpresionRecepcion(recepcion: any, cliente: any) {
  const imprimir = (formato: 'a4' | 'ticket') => {
    const container = document.createElement('div')
    container.style.display = 'none'
    document.body.appendChild(container)

    const component = formato === 'a4'
      ? createVNode(OrdenRecepcionA4, { recepcion, cliente })
      : createVNode(OrdenRecepcionTicket, { recepcion, cliente })

    render(component, container)

    setTimeout(() => {
      const printWindow = window.open('', '', 'height=600,width=800')
      if (printWindow) {
        printWindow.document.write('<html><head><title>Impresión</title></head><body>')
        printWindow.document.write(container.innerHTML)
        printWindow.document.write('</body></html>')
        printWindow.document.close()
        printWindow.print()
      }
      render(null, container)
      document.body.removeChild(container)
    }, 200)
  }

  return { imprimir }
}
